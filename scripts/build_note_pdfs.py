from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
HTML_OUT = ROOT / "output" / "html"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def note_number(path: Path) -> int:
    match = re.search(r"Note(\d+)\.md$", path.name)
    return int(match.group(1)) if match else 0


def split_rows(source: str) -> list[str]:
    rows: list[str] = []
    current: list[str] = []
    depth = 0
    i = 0
    while i < len(source):
        if source.startswith(r"\begin", i):
            depth += 1
            current.append(source[i])
            i += 1
            continue
        if source.startswith(r"\end", i):
            depth = max(0, depth - 1)
            current.append(source[i])
            i += 1
            continue
        if source.startswith(r"\\", i) and depth == 0:
            row = "".join(current).strip()
            if row:
                rows.append(row)
            current = []
            i += 2
            continue
        current.append(source[i])
        i += 1
    row = "".join(current).strip()
    if row:
        rows.append(row)
    return rows


def split_cells(row: str) -> list[str]:
    cells: list[str] = []
    current: list[str] = []
    depth = 0
    i = 0
    while i < len(row):
        if row.startswith(r"\begin", i):
            depth += 1
            current.append(row[i])
            i += 1
            continue
        if row.startswith(r"\end", i):
            depth = max(0, depth - 1)
            current.append(row[i])
            i += 1
            continue
        if row[i] == "&" and depth == 0:
            cells.append("".join(current).strip())
            current = []
            i += 1
            continue
        current.append(row[i])
        i += 1
    cells.append("".join(current).strip())
    return cells


def clean_math(source: str) -> str:
    source = source.strip()
    source = source.replace(r"\quad", "  ")
    source = source.replace(r"\qquad", "    ")
    source = source.replace(r"\,", " ")
    return source


def plain_math(source: str) -> str:
    source = clean_math(source)
    replacements = {
        r"\det": "det",
        r"\operatorname": "",
        r"\Longleftrightarrow": "⟺",
        r"\longrightarrow": "→",
        r"\leftarrow": "←",
        r"\rightarrow": "→",
        r"\ne": "≠",
        r"\cdots": "⋯",
        r"\vdots": "⋮",
        r"\frac": "frac",
        r"\times": "×",
        r"\cdot": "·",
        r"\pm": "±",
    }
    for old, new in replacements.items():
        source = source.replace(old, new)

    source = re.sub(r"frac\{([^{}]+)\}\{([^{}]+)\}", r"<span class='frac'><span>\1</span><span>\2</span></span>", source)
    source = re.sub(r"\^\{([^{}]+)\}", r"<sup>\1</sup>", source)
    source = re.sub(r"_\{([^{}]+)\}", r"<sub>\1</sub>", source)
    source = re.sub(r"\^([A-Za-z0-9+-]+)", r"<sup>\1</sup>", source)
    source = re.sub(r"_([A-Za-z0-9+-]+)", r"<sub>\1</sub>", source)
    source = source.replace("{", "").replace("}", "")
    return source


def table_from_rows(rows: list[list[str]], kind: str, spec: str = "") -> str:
    separators = {idx for idx, char in enumerate(spec) if char == "|"}
    cells = []
    for row in rows:
        rendered = []
        for index, cell in enumerate(row):
            classes = ["mcell"]
            if index in separators:
                classes.append("vbar-left")
            rendered.append(f"<td class='{' '.join(classes)}'>{math_html(cell)}</td>")
        cells.append("<tr>" + "".join(rendered) + "</tr>")

    open_mark, close_mark = {
        "pmatrix": ("(", ")"),
        "vmatrix": ("|", "|"),
        "matrix": ("", ""),
        "array": ("", ""),
    }.get(kind, ("", ""))

    return (
        f"<span class='matrix-wrap {kind}'>"
        f"<span class='matrix-bracket'>{open_mark}</span>"
        f"<table class='matrix'><tbody>{''.join(cells)}</tbody></table>"
        f"<span class='matrix-bracket'>{close_mark}</span>"
        f"</span>"
    )


def render_environment(source: str) -> str | None:
    source = clean_math(source)

    match = re.fullmatch(r"\\begin\{(p?matrix|vmatrix)\}(.+?)\\end\{\1\}", source, re.S)
    if match:
        kind, body = match.groups()
        rows = [split_cells(row) for row in split_rows(body)]
        return table_from_rows(rows, kind)

    match = re.fullmatch(r"\\begin\{array\}\{([^{}]*)\}(.+?)\\end\{array\}", source, re.S)
    if match:
        spec, body = match.groups()
        rows = [split_cells(row) for row in split_rows(body)]
        return table_from_rows(rows, "array", spec)

    match = re.fullmatch(r"\\left\((\\begin\{array\}\{[^{}]*\}.+?\\end\{array\})\\right\)", source, re.S)
    if match:
        inner = render_environment(match.group(1))
        return f"<span class='matrix-wrap pmatrix'><span class='matrix-bracket'>(</span>{inner}<span class='matrix-bracket'>)</span></span>"

    match = re.fullmatch(r"\\begin\{cases\}(.+?)\\end\{cases\}", source, re.S)
    if match:
        rows = [split_cells(row) for row in split_rows(match.group(1))]
        body = "".join(
            "<tr>" + "".join(f"<td class='case-cell'>{math_html(cell)}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        return f"<span class='cases'><span class='case-brace'>{{</span><table><tbody>{body}</tbody></table></span>"

    match = re.fullmatch(r"\\begin\{aligned\}(.+?)\\end\{aligned\}", source, re.S)
    if match:
        rows = [split_cells(row) for row in split_rows(match.group(1))]
        body = "".join(
            "<tr>" + "".join(f"<td class='align-cell'>{math_html(cell)}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        return f"<table class='aligned'><tbody>{body}</tbody></table>"

    return None


ENV_PATTERNS = [
    re.compile(r"\\left\((\\begin\{array\}\{[^{}]*\}.+?\\end\{array\})\\right\)", re.S),
    re.compile(r"\\begin\{(pmatrix|matrix|vmatrix)\}(.+?)\\end\{\1\}", re.S),
    re.compile(r"\\begin\{array\}\{([^{}]*)\}(.+?)\\end\{array\}", re.S),
    re.compile(r"\\begin\{cases\}(.+?)\\end\{cases\}", re.S),
    re.compile(r"\\begin\{aligned\}(.+?)\\end\{aligned\}", re.S),
]


def first_environment(source: str) -> tuple[re.Match[str], re.Pattern[str]] | None:
    found: tuple[re.Match[str], re.Pattern[str]] | None = None
    for pattern in ENV_PATTERNS:
        match = pattern.search(source)
        if match and (found is None or match.start() < found[0].start()):
            found = (match, pattern)
    return found


def render_environment_match(match: re.Match[str], pattern: re.Pattern[str]) -> str:
    pattern_index = ENV_PATTERNS.index(pattern)
    if pattern_index == 0:
        inner = render_environment(match.group(1)) or math_html(match.group(1))
        return f"<span class='matrix-wrap pmatrix'><span class='matrix-bracket'>(</span>{inner}<span class='matrix-bracket'>)</span></span>"
    if pattern_index == 1:
        kind, body = match.groups()
        return table_from_rows([split_cells(row) for row in split_rows(body)], kind)
    if pattern_index == 2:
        spec, body = match.groups()
        return table_from_rows([split_cells(row) for row in split_rows(body)], "array", spec)
    if pattern_index == 3:
        rows = [split_cells(row) for row in split_rows(match.group(1))]
        body = "".join(
            "<tr>" + "".join(f"<td class='case-cell'>{math_html(cell)}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        return f"<span class='cases'><span class='case-brace'>{{</span><table><tbody>{body}</tbody></table></span>"
    rows = [split_cells(row) for row in split_rows(match.group(1))]
    body = "".join(
        "<tr>" + "".join(f"<td class='align-cell'>{math_html(cell)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    return f"<table class='aligned'><tbody>{body}</tbody></table>"


def math_html(source: str) -> str:
    source = clean_math(source)
    found = first_environment(source)
    if not found:
        return plain_math(source)

    match, pattern = found
    before = plain_math(source[: match.start()])
    rendered = render_environment_match(match, pattern)
    after = math_html(source[match.end() :])
    return before + rendered + after


def render_math_block(source: str) -> str:
    source = clean_math(source)
    if first_environment(source):
        return f"<div class='math-block'><span class='formula'>{math_html(source)}</span></div>"

    # Render multi-line equations as aligned math rows instead of raw TeX.
    rows = split_rows(source)
    if len(rows) > 1:
        body = "".join(
            "<tr>" + "".join(f"<td class='align-cell'>{math_html(cell)}</td>" for cell in split_cells(row)) + "</tr>"
            for row in rows
        )
        return f"<div class='math-block'><table class='aligned'><tbody>{body}</tbody></table></div>"

    return f"<div class='math-block'><span class='formula'>{math_html(source)}</span></div>"


def inline_markup(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"<u>\1</u>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\$([^$]+)\$", lambda m: f"<span class='inline-math'>{math_html(html.unescape(m.group(1)))}</span>", escaped)
    return escaped


def render_markdown(markdown: str) -> str:
    lines = markdown.splitlines()
    parts: list[str] = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        if stripped == "---":
            parts.append("<hr>")
            i += 1
            continue

        if stripped == "$$":
            buf: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != "$$":
                buf.append(lines[i])
                i += 1
            i += 1
            parts.append(render_math_block("\n".join(buf)))
            continue

        if stripped.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            parts.append(f"<pre>{html.escape(chr(10).join(buf))}</pre>")
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = lines[i].strip().strip("|")
                rows.append([cell.strip() for cell in row.split("|")])
                i += 1
            if len(rows) > 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]):
                rows.pop(1)
            table_rows = []
            for row_index, row in enumerate(rows):
                tag = "th" if row_index == 0 else "td"
                table_rows.append("<tr>" + "".join(f"<{tag}>{inline_markup(cell)}</{tag}>" for cell in row) + "</tr>")
            parts.append(f"<table class='data'><tbody>{''.join(table_rows)}</tbody></table>")
            continue

        if stripped.startswith("# "):
            parts.append(f"<h1>{inline_markup(stripped[2:].strip())}</h1>")
            i += 1
            continue

        if stripped.startswith("## "):
            parts.append(f"<h2>{inline_markup(stripped[3:].strip())}</h2>")
            i += 1
            continue

        if stripped.startswith("### "):
            parts.append(f"<h3>{inline_markup(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(f"<li>{inline_markup(re.sub(r'^[-*]\\s+', '', lines[i].strip()))}</li>")
                i += 1
            parts.append(f"<ul>{''.join(items)}</ul>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(f"<li>{inline_markup(re.sub(r'^\\d+\\.\\s+', '', lines[i].strip()))}</li>")
                i += 1
            parts.append(f"<ol>{''.join(items)}</ol>")
            continue

        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt == "---" or nxt == "$$" or nxt.startswith(("#", "```", "|")) or re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+\.\s+", nxt):
                break
            paragraph.append(nxt)
            i += 1
        parts.append(f"<p>{inline_markup(' '.join(paragraph))}</p>")

    return "\n".join(parts)


CSS = """
@page { size: A4; margin: 16mm 15mm 17mm; }
* { box-sizing: border-box; }
body {
  font-family: "Noto Sans JP", "Yu Gothic", "Meiryo", sans-serif;
  color: #111827;
  line-height: 1.72;
  font-size: 10.8pt;
}
h1 {
  text-align: center;
  font-size: 21pt;
  line-height: 1.35;
  margin: 0 0 14pt;
  color: #0f172a;
}
h2 {
  break-after: avoid;
  font-size: 15pt;
  margin: 18pt 0 7pt;
  padding-bottom: 3pt;
  border-bottom: 1px solid #dbe3ef;
  color: #0f172a;
}
h3 {
  break-after: avoid;
  font-size: 12.4pt;
  margin: 12pt 0 4pt;
  color: #1f2937;
}
p { margin: 0 0 6pt; }
ul, ol { margin: 4pt 0 8pt 18pt; padding: 0; }
li { margin: 1.5pt 0; }
hr { border: 0; border-top: 1px solid #e5e7eb; margin: 11pt 0; }
code {
  font-family: "Cascadia Mono", Consolas, monospace;
  background: #f3f4f6;
  padding: 1px 3px;
  border-radius: 3px;
}
pre {
  white-space: pre-wrap;
  font-family: "Cascadia Mono", Consolas, monospace;
  font-size: 8.7pt;
  line-height: 1.35;
  background: #f8fafc;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  padding: 7pt;
  margin: 5pt 0 8pt;
}
table.data {
  width: 100%;
  border-collapse: collapse;
  margin: 6pt 0 9pt;
  break-inside: avoid;
}
table.data th, table.data td {
  border: 1px solid #cbd5e1;
  padding: 4pt 5pt;
  vertical-align: top;
}
table.data th { background: #eef2ff; text-align: left; }
.inline-math, .formula {
  font-family: "Cambria Math", "Times New Roman", serif;
  font-size: 1.02em;
}
.math-block {
  text-align: center;
  margin: 7pt auto 10pt;
  break-inside: avoid;
  font-family: "Cambria Math", "Times New Roman", "Noto Sans JP", serif;
  font-size: 12.2pt;
}
.matrix-wrap {
  display: inline-flex;
  align-items: stretch;
  vertical-align: middle;
  gap: 2px;
}
.matrix-wrap.array { align-items: center; }
.matrix-wrap.vmatrix .matrix-bracket { font-weight: 300; }
.matrix-bracket {
  display: inline-flex;
  align-items: center;
  font-size: 2.7em;
  line-height: 1;
  padding: 0 1px;
}
table.matrix, table.aligned, .cases table {
  display: inline-table;
  border-collapse: collapse;
  vertical-align: middle;
}
.mcell {
  min-width: 1.45em;
  padding: 1px 5px;
  text-align: center;
  white-space: nowrap;
}
.vbar-left { border-left: 1.5px solid #111827; }
table.aligned { text-align: left; }
.align-cell {
  padding: 1px 5px;
  white-space: nowrap;
  text-align: left;
}
.align-cell:first-child { text-align: right; }
.cases {
  display: inline-flex;
  align-items: stretch;
  gap: 4px;
}
.case-brace {
  display: inline-flex;
  align-items: center;
  font-size: 2.8em;
  line-height: 1;
}
.case-cell {
  padding: 1px 5px;
  text-align: left;
  white-space: nowrap;
}
.frac {
  display: inline-flex;
  flex-direction: column;
  vertical-align: middle;
  text-align: center;
  line-height: 1.05;
  margin: 0 2px;
}
.frac span:first-child {
  border-bottom: 1px solid currentColor;
  padding: 0 2px 1px;
}
.frac span:last-child { padding-top: 1px; }
.footer {
  position: running(footer);
}
"""


def build_html(note: Path) -> Path:
    number = note_number(note)
    body = render_markdown(note.read_text(encoding="utf-8"))
    html_text = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>senkei_note_{number:02d}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
    out = HTML_OUT / f"senkei_note_{number:02d}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, encoding="utf-8")
    return out


def print_pdf(html_path: Path, pdf_path: Path) -> None:
    if not CHROME.exists():
        raise RuntimeError(f"Chrome not found: {CHROME}")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(CHROME),
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)


def combine_pdfs(pdf_paths: list[Path], combined: Path) -> None:
    writer = PdfWriter()
    for path in pdf_paths:
        reader = PdfReader(str(path))
        for page in reader.pages:
            writer.add_page(page)
    with combined.open("wb") as handle:
        writer.write(handle)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    HTML_OUT.mkdir(parents=True, exist_ok=True)

    notes = sorted(ROOT.glob("第*回/Note*.md"), key=note_number)
    if not notes:
        print("No note files found.", file=sys.stderr)
        return 1

    pdfs: list[Path] = []
    for note in notes:
        number = note_number(note)
        html_path = build_html(note)
        pdf_path = OUT / f"senkei_note_{number:02d}.pdf"
        print_pdf(html_path, pdf_path)
        pdfs.append(pdf_path)

    combined = OUT / "senkei_all_notes.pdf"
    combine_pdfs(pdfs, combined)

    for path in [*pdfs, combined]:
        pages = len(PdfReader(str(path)).pages)
        print(f"{path.relative_to(ROOT)}\tpages={pages}\tsize={path.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
