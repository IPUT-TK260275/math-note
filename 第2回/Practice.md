# 線形代数 第2回 Practice：行列式と逆行列

この小テストが一通り解ければ、第2回の内容は満点を狙える。
各Methodは5問ずつ。逆行列では、必ず先に行列式を確認すること。

---

## Method 1：行列式を計算する

### 問題

1. 次を求めよ。

$$
|-7|
$$

2. 次を求めよ。

$$
\begin{vmatrix}
2 & 5 \\
1 & 3
\end{vmatrix}
$$

3. 次を求めよ。

$$
\begin{vmatrix}
-1 & 4 \\
2 & 6
\end{vmatrix}
$$

4. 次を求めよ。

$$
\begin{vmatrix}
0 & 3 \\
-2 & 5
\end{vmatrix}
$$

5. 次の行列式の公式を書け。

$$
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
$$

### 解答

1. $-7$
2. $2 \times 3 - 5 \times 1 = 1$
3. $(-1) \times 6 - 4 \times 2 = -14$
4. $0 \times 5 - 3 \times (-2) = 6$
5. $ad-bc$

---

## Method 2：逆行列が存在するか判定する

### 問題

次の行列について、逆行列が存在するか判定せよ。

1.

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
2 & 4 \\
1 & 2
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
0 & 1 \\
-3 & 2
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
5 & -1 \\
10 & -2
\end{pmatrix}
$$

5.

$$
\begin{pmatrix}
-2 & 3 \\
4 & 1
\end{pmatrix}
$$

### 解答

1. $\det A=-2$ なので存在する。
2. $\det A=0$ なので存在しない。
3. $\det A=3$ なので存在する。
4. $\det A=0$ なので存在しない。
5. $\det A=-14$ なので存在する。

---

## Method 3：2次正方行列の逆行列を求める

### 問題

次の行列の逆行列を求めよ。

1.

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

2.

$$
A =
\begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
$$

3.

$$
A =
\begin{pmatrix}
3 & 1 \\
5 & 2
\end{pmatrix}
$$

4.

$$
A =
\begin{pmatrix}
0 & 2 \\
1 & 3
\end{pmatrix}
$$

5.

$$
A =
\begin{pmatrix}
5 & 3 \\
1 & -1
\end{pmatrix}
$$

### 解答

1.

$$
A^{-1} =
\begin{pmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{pmatrix}
$$

2.

$$
A^{-1} =
\begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
$$

3.

$$
A^{-1} =
\begin{pmatrix}
2 & -1 \\
-5 & 3
\end{pmatrix}
$$

4.

$$
A^{-1} =
\begin{pmatrix}
-\frac{3}{2} & 1 \\
\frac{1}{2} & 0
\end{pmatrix}
$$

5.

$$
A^{-1} =
\frac{1}{8}
\begin{pmatrix}
1 & 3 \\
1 & -5
\end{pmatrix}
$$

---

## Method 4：逆行列を確かめる

### 問題

1. 次の $AX$ を計算し、$X$ が $A^{-1}$ か確認せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
X =
\begin{pmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{pmatrix}
$$

2. 問題1の $XA$ を計算し、$X$ が $A^{-1}$ か確認せよ。

3. 次の $AX$ を計算し、$X$ が $A^{-1}$ か確認せよ。

$$
A =
\begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix},
\qquad
X =
\begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
$$

4. 次の $X$ は $A$ の逆行列か答えよ。

$$
A =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix},
\qquad
X =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

5. $AX=E$ かつ $XA=E$ が成り立つとき、$X$ は何と呼ばれるか答えよ。

### 解答

1.

$$
AX =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
=E
$$

2.

$$
XA =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
=E
$$

したがって、$X=A^{-1}$ である。

3.

$$
AX =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
=E
$$

4. $AX=A$ であり $E$ にならないので、$X$ は $A$ の逆行列ではない。
5. $A$ の逆行列

---

## Method 5：行列の積の順番に注意する

### 問題

1. $AB$ を計算せよ。

$$
A =
\begin{pmatrix}
4 & 0 \\
-3 & 1
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
$$

2. 問題1の $BA$ を計算せよ。

3. 問題1の $A,B$ について、$AB=BA$ といえるか答えよ。

4. $CD$ と $DC$ を計算せよ。

$$
C =
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix},
\qquad
D =
\begin{pmatrix}
1 & 0 \\
3 & 1
\end{pmatrix}
$$

5. 逆行列の確認で $AA^{-1}$ と $A^{-1}A$ の両方を見る理由を一言で答えよ。

### 解答

1.

$$
AB =
\begin{pmatrix}
4 & 0 \\
-3 & 2
\end{pmatrix}
$$

2.

$$
BA =
\begin{pmatrix}
4 & 0 \\
-6 & 2
\end{pmatrix}
$$

3. 左下の成分が違うので、$AB=BA$ とはいえない。

4.

$$
CD =
\begin{pmatrix}
7 & 2 \\
3 & 1
\end{pmatrix},
\qquad
DC =
\begin{pmatrix}
1 & 2 \\
3 & 7
\end{pmatrix}
$$

5. 行列の掛け算は、順番を変えると結果が変わることがあるから。

