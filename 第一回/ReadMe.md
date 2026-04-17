# 線形代数 1：行列の基礎ノート

## 1. 授業の目的

この授業では、線形代数の入口として **行列** を学ぶ。

行列は、AI、画像処理、データ処理、プログラミング、専門科目などで使われる大事な考え方である。

今日の目標は、次のことができるようになること。

* 行列とは何かを理解する
* 行列の大きさを読めるようにする
* 成分の場所を指定できるようにする
* 行列の足し算・引き算ができるようにする
* 行列の掛け算のルールを理解する
* 行列では、掛け算の順番が大事だと理解する

---

## 2. 行列とは

行列とは、数字を **行** と **列** に並べたもの。

例：

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

このように、数字をカッコで囲んで書く。

---

## 3. 行と列

### 行

横方向を **行** という。

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

この行列では、

* (1,2) が **1行目**
* (3,4) が **2行目**

### 列

縦方向を **列** という。

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

この行列では、

* (1,3) が **1列目**
* (2,4) が **2列目**

### 覚え方

行列の大きさは、必ず

[
行 \times 列
]

の順番で読む。

つまり、**先に行、あとに列**。

---

## 4. 行列の大きさ

### 例1

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

これは、

* 2行
* 2列

なので、

[
2 \times 2 行列
]

という。

また、正方形の形なので **2次正方行列** ともいう。

---

### 例2

[
\begin{pmatrix}
1 & 2 & 3 \
4 & 5 & 6 \
7 & 8 & 9
\end{pmatrix}
]

これは、

* 3行
* 3列

なので、

[
3 \times 3 行列
]

または **3次正方行列** という。

---

### 例3

[
\begin{pmatrix}
1 & 2 & 3 \
4 & 5 & 6
\end{pmatrix}
]

これは、

* 2行
* 3列

なので、

[
2 \times 3 行列
]

という。

正方形ではないので、**長方行列** と呼ぶこともある。

---

## 5. 成分とは

行列の中に入っている一つ一つの数字を **成分** という。

例：

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4 \
5 & 6
\end{pmatrix}
]

このとき、

* (1), (2), (3), (4), (5), (6) が成分

---

## 6. 成分の場所の読み方

成分の場所は、

[
行番号, 列番号
]

で表す。

### 例

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4 \
5 & 6
\end{pmatrix}
]

### 問題

(A) の ((3,1)) 成分の値は？

### 解き方

((3,1)) 成分とは、

* 3行目
* 1列目

の数字を指す。

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4 \
\color{red}{5} & 6
\end{pmatrix}
]

したがって、

[
(3,1)成分 = 5
]

---

## 7. 行列の足し算

行列の足し算は、**同じ場所の成分どうしを足す**。

### 例

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix},
B=
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

[
A+B=
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
+
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

同じ場所どうしを足す。

# [

\begin{pmatrix}
1+5 & 2+6 \
3+7 & 4+8
\end{pmatrix}
]

# [

\begin{pmatrix}
6 & 8 \
10 & 12
\end{pmatrix}
]

### ポイント

足し算できるのは、行列の大きさが同じときだけ。

[
2 \times 2 + 2 \times 2
]

は計算できる。

しかし、

[
2 \times 2 + 3 \times 2
]

のように形が違うものは計算できない。

---

## 8. 行列の引き算

行列の引き算も、**同じ場所の成分どうしを引く**。

### 例

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix},
B=
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

[
B-A=
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
-------------

\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

# [

\begin{pmatrix}
5-1 & 6-2 \
7-3 & 8-4
\end{pmatrix}
]

# [

\begin{pmatrix}
4 & 4 \
4 & 4
\end{pmatrix}
]

---

## 9. 行列の前に数字があるとき

行列の前に数字があるときは、行列の中のすべての成分にその数字をかける。

### 例

[
4
\begin{pmatrix}
1 & 1 \
1 & 1
\end{pmatrix}
=============

\begin{pmatrix}
4 & 4 \
4 & 4
\end{pmatrix}
]

逆に、すべての成分に共通の数字があるときは、外に出せる。

[
\begin{pmatrix}
4 & 4 \
4 & 4
\end{pmatrix}
=============

4
\begin{pmatrix}
1 & 1 \
1 & 1
\end{pmatrix}
]

---

## 10. 例題：(2B-3A)

[
A=
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix},
B=
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

[
2B-3A
=2
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
-3
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
]

まず、それぞれ中にかける。

# [

\begin{pmatrix}
10 & 12 \
14 & 16
\end{pmatrix}
-------------

\begin{pmatrix}
3 & 6 \
9 & 12
\end{pmatrix}
]

同じ場所どうしを引く。

# [

\begin{pmatrix}
10-3 & 12-6 \
14-9 & 16-12
\end{pmatrix}
]

# [

\begin{pmatrix}
7 & 6 \
5 & 4
\end{pmatrix}
]

---

## 11. 単位行列

対角成分がすべて (1)、それ以外が (0) の行列を **単位行列** という。

### 2次の単位行列

[
E=
\begin{pmatrix}
1 & 0 \
0 & 1
\end{pmatrix}
]

### 3次の単位行列

[
E=
\begin{pmatrix}
1 & 0 & 0 \
0 & 1 & 0 \
0 & 0 & 1
\end{pmatrix}
]

### ポイント

単位行列は、普通の数でいう **1** のような役割をする行列。

---

## 12. ゼロ行列

すべての成分が (0) の行列を **ゼロ行列** という。

例：

[
O=
\begin{pmatrix}
0 & 0 \
0 & 0
\end{pmatrix}
]

### 例

同じ行列を引くと、ゼロ行列になる。

[
A-A=O
]

具体的には、

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
-------------

\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
=============

\begin{pmatrix}
0 & 0 \
0 & 0
\end{pmatrix}
]

---

## 13. 行列の掛け算ができる条件

行列の掛け算は、足し算・引き算よりルールが厳しい。

[
(m \times n) \times (n \times p)
]

のように、**左の行列の列数** と **右の行列の行数** が同じときだけ計算できる。

### 例

[
(3 \times 2) \times (2 \times 4)
]

真ん中の (2) と (2) が同じなので計算できる。

答えの形は、外側の数字を使って、

[
3 \times 4
]

になる。

### 形の見方

[
(3 \times \cancel{2}) \times (\cancel{2} \times 4)
]

真ん中が一致するので計算できる。

残った外側が答えの形。

[
3 \times 4
]

---

## 14. 掛け算できない例

[
(3 \times 2) \times (1 \times 4)
]

この場合、真ん中が

[
2 \neq 1
]

なので計算できない。

---

## 15. 行列の掛け算のやり方

行列の掛け算は、

* 左の行列は **横** に見る
* 右の行列は **縦** に見る

これが基本。

### 例

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

答えは (2 \times 2) 行列になる。

# [

\begin{pmatrix}
? & ? \
? & ?
\end{pmatrix}
]

---

### 左上の成分

左上は、

* 左の行列の1行目
* 右の行列の1列目

を使う。

[
1 \times 5 + 2 \times 7
]

[
=5+14=19
]

---

### 右上の成分

右上は、

* 左の行列の1行目
* 右の行列の2列目

を使う。

[
1 \times 6 + 2 \times 8
]

[
=6+16=22
]

---

### 左下の成分

左下は、

* 左の行列の2行目
* 右の行列の1列目

を使う。

[
3 \times 5 + 4 \times 7
]

[
=15+28=43
]

---

### 右下の成分

右下は、

* 左の行列の2行目
* 右の行列の2列目

を使う。

[
3 \times 6 + 4 \times 8
]

[
=18+32=50
]

---

### したがって

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
=============

\begin{pmatrix}
19 & 22 \
43 & 50
\end{pmatrix}
]

---

## 16. 掛け算の覚え方

行列の掛け算は、

[
左は横、右は縦
]

で見る。

そして、対応する数字をかけて、最後に足す。

### 左上なら

[
左の1行目 \times 右の1列目
]

### 右上なら

[
左の1行目 \times 右の2列目
]

### 左下なら

[
左の2行目 \times 右の1列目
]

### 右下なら

[
左の2行目 \times 右の2列目
]

---

## 17. 行列の掛け算は順番が大事

普通の数字では、

[
2 \times 3 = 3 \times 2
]

となる。

しかし、行列では基本的に

[
AB \neq BA
]

になる。

つまり、**Aを先にかけるか、Bを先にかけるかで答えが変わる**。

---

## 18. 例：(AB) と (BA) の違い

[
A=
\begin{pmatrix}
4 & 0 \
-3 & 1
\end{pmatrix},
B=
\begin{pmatrix}
1 & 0 \
0 & 2
\end{pmatrix}
]

---

### (AB)

[
AB=
\begin{pmatrix}
4 & 0 \
-3 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \
0 & 2
\end{pmatrix}
]

# [

\begin{pmatrix}
4 & 0 \
-3 & 2
\end{pmatrix}
]

---

### (BA)

[
BA=
\begin{pmatrix}
1 & 0 \
0 & 2
\end{pmatrix}
\begin{pmatrix}
4 & 0 \
-3 & 1
\end{pmatrix}
]

# [

\begin{pmatrix}
4 & 0 \
-6 & 2
\end{pmatrix}
]

---

### 比較

[
AB=
\begin{pmatrix}
4 & 0 \
-3 & 2
\end{pmatrix}
]

[
BA=
\begin{pmatrix}
4 & 0 \
-6 & 2
\end{pmatrix}
]

左下の成分が違う。

したがって、

[
AB \neq BA
]

---

## 19. ((A+B)(A-B)) の展開

普通の数なら、

[
(A+B)(A-B)=A^2-B^2
]

となる。

しかし、行列では注意が必要。

行列では、掛け算の順番が変わると答えも変わるため、

[
AB \neq BA
]

だからである。

---

### 展開する

[
(A+B)(A-B)
]

左側の (A+B) を、それぞれ右側にかける。

[
=A(A-B)+B(A-B)
]

さらに展開する。

[
=A^2-AB+BA-B^2
]

---

### 重要ポイント

ここで、

[
-AB+BA
]

は、基本的に (0) にならない。

なぜなら、

[
AB \neq BA
]

だから。

したがって、行列では

[
(A+B)(A-B)=A^2-AB+BA-B^2
]

であり、普通の数のように簡単に

[
A^2-B^2
]

とはできない。

---

## 20. 例：((A+B)(A-B)) の計算

[
A=
\begin{pmatrix}
4 & 0 \
-3 & 1
\end{pmatrix},
B=
\begin{pmatrix}
1 & 0 \
0 & 2
\end{pmatrix}
]

このとき、

[
(A+B)(A-B)
=A^2-AB+BA-B^2
]

各部分は、

[
A^2=
\begin{pmatrix}
16 & 0 \
-15 & 1
\end{pmatrix}
]

[
AB=
\begin{pmatrix}
4 & 0 \
-3 & 2
\end{pmatrix}
]

[
BA=
\begin{pmatrix}
4 & 0 \
-6 & 2
\end{pmatrix}
]

[
B^2=
\begin{pmatrix}
1 & 0 \
0 & 4
\end{pmatrix}
]

したがって、

[
A^2-AB+BA-B^2
]

# [

\begin{pmatrix}
16 & 0 \
-15 & 1
\end{pmatrix}
-------------

\begin{pmatrix}
4 & 0 \
-3 & 2
\end{pmatrix}
+
\begin{pmatrix}
4 & 0 \
-6 & 2
\end{pmatrix}
-------------

\begin{pmatrix}
1 & 0 \
0 & 4
\end{pmatrix}
]

# [

\begin{pmatrix}
15 & 0 \
-18 & -3
\end{pmatrix}
]

---

## 21. ノートの取り方のポイント

先生が強調していた大事なこと。

### 1. 計算過程を必ず書く

数学が苦手な人ほど、途中式を飛ばして間違えやすい。

上のクラスの学生は、計算過程を丁寧に書いている。

だから、途中式を省略しないことが大事。

---

### 2. イコールを縦にそろえる

横にどんどん書いていくと、どこで何を計算したのか分かりにくくなる。

例：

[
A+B
===

\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
+
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

# [

\begin{pmatrix}
1+5 & 2+6 \
3+7 & 4+8
\end{pmatrix}
]

# [

\begin{pmatrix}
6 & 8 \
10 & 12
\end{pmatrix}
]

このように、イコールを縦にそろえると見やすい。

---

### 3. 行列は大きく書く

行列は数字が近すぎると、どの数字がどの場所にあるのか分からなくなる。

そのため、行列は少し大きめに、余白を空けて書く。

---

## 22. 今日の最重要まとめ

今日の内容で特に大事なのは、次の5つ。

### 1. 行列の大きさは「行 × 列」

[
2 \times 3 行列
]

なら、2行3列。

---

### 2. 成分は「行番号、列番号」で指定する

((3,1)) 成分なら、3行1列目。

---

### 3. 足し算・引き算は同じ場所どうし

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
+
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
=============

\begin{pmatrix}
6 & 8 \
10 & 12
\end{pmatrix}
]

---

### 4. 掛け算は「左は横、右は縦」

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
=============

\begin{pmatrix}
19 & 22 \
43 & 50
\end{pmatrix}
]

---

### 5. 行列では (AB) と (BA) は基本的に違う

[
AB \neq BA
]

これが普通の数との大きな違い。

---

## 23. 復習用ミニ問題

### 問題1

次の行列の大きさを答えよ。

[
\begin{pmatrix}
1 & 2 & 3 \
4 & 5 & 6
\end{pmatrix}
]

答え：

[
2 \times 3 行列
]

---

### 問題2

次の行列の ((2,1)) 成分を答えよ。

[
\begin{pmatrix}
1 & 2 \
3 & 4 \
5 & 6
\end{pmatrix}
]

答え：

[
3
]

---

### 問題3

計算せよ。

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
+
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

答え：

[
\begin{pmatrix}
6 & 8 \
10 & 12
\end{pmatrix}
]

---

### 問題4

計算せよ。

[
\begin{pmatrix}
1 & 2 \
3 & 4
\end{pmatrix}
\begin{pmatrix}
5 & 6 \
7 & 8
\end{pmatrix}
]

答え：

[
\begin{pmatrix}
19 & 22 \
43 & 50
\end{pmatrix}
]

---

## 24. この授業で覚える言葉

| 用語   | 意味               |
| ---- | ---------------- |
| 行    | 横方向              |
| 列    | 縦方向              |
| 成分   | 行列の中の数字          |
| 正方行列 | 行数と列数が同じ行列       |
| 長方行列 | 行数と列数が違う行列       |
| 単位行列 | 対角成分が1、それ以外が0の行列 |
| ゼロ行列 | すべての成分が0の行列      |
| 対角成分 | 左上から右下に並ぶ成分      |

