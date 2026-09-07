# 線形代数 第5回 Practice：掃き出し法と階数

この小テストが一通り解ければ、第5回の内容は満点を狙える。
各Methodは5問ずつ。逆行列は左側が単位行列になるまで、階数は0でない行の本数が分かるまで変形する。

---

## Method 1：逆行列の公式を復習する

### 問題

1. 次の行列式を求めよ。

$$
\begin{vmatrix}
3 & 4 \\
2 & 3
\end{vmatrix}
$$

2. 次の行列の逆行列を公式で求めよ。

$$
A=
\begin{pmatrix}
3 & 4 \\
2 & 3
\end{pmatrix}
$$

3. 次の行列式を求めよ。

$$
\begin{vmatrix}
1 & -3 \\
-2 & 5
\end{vmatrix}
$$

4. 次の行列の逆行列を公式で求めよ。

$$
A=
\begin{pmatrix}
1 & -3 \\
-2 & 5
\end{pmatrix}
$$

5. 2次正方行列の逆行列が存在する条件を答えよ。

### 解答

1. $1$

2.

$$
A^{-1}
=
\begin{pmatrix}
3 & -4 \\
-2 & 3
\end{pmatrix}
$$

3. $-1$

4.

$$
A^{-1}
=
\begin{pmatrix}
-5 & -3 \\
-2 & -1
\end{pmatrix}
$$

5. $\det A \ne 0$

---

## Method 2：掃き出し法で逆行列を求める

### 問題

1. 掃き出し法で逆行列を求めるとき、最初に作る行列を書け。

$$
A=
\begin{pmatrix}
3 & 4 \\
2 & 3
\end{pmatrix}
$$

2. 次の変形の右側から、$A^{-1}$ を答えよ。

$$
\left(
\begin{array}{cc|cc}
1 & 0 & 3 & -4 \\
0 & 1 & -2 & 3
\end{array}
\right)
$$

3. 掃き出し法で逆行列を求めるとき、左側は最終的に何行列にするか答えよ。

4. 次の行列の逆行列を掃き出し法で求めよ。

$$
A=
\begin{pmatrix}
1 & 2 \\
1 & 3
\end{pmatrix}
$$

5. 次の行列の逆行列を求めよ。

$$
B=
\begin{pmatrix}
2 & -5 \\
1 & -3
\end{pmatrix}
$$

### 解答

1.

$$
\left(
\begin{array}{cc|cc}
3 & 4 & 1 & 0 \\
2 & 3 & 0 & 1
\end{array}
\right)
$$

2.

$$
A^{-1}
=
\begin{pmatrix}
3 & -4 \\
-2 & 3
\end{pmatrix}
$$

3. 単位行列

4.

$$
A^{-1}
=
\begin{pmatrix}
3 & -2 \\
-1 & 1
\end{pmatrix}
$$

5.

$$
B^{-1}
=
\begin{pmatrix}
3 & -5 \\
1 & -2
\end{pmatrix}
$$

---

## Method 3：3次正方行列の逆行列を読む

### 問題

1. 次の行列で、右に並べる単位行列を書け。

$$
A=
\begin{pmatrix}
1 & 0 & 0 \\
-3 & 1 & 0 \\
0 & -3 & 1
\end{pmatrix}
$$

2. 次の掃き出し結果から、$A^{-1}$ を答えよ。

$$
\left(
\begin{array}{ccc|ccc}
1 & 0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 3 & 1 & 0 \\
0 & 0 & 1 & 9 & 3 & 1
\end{array}
\right)
$$

3. 次の行列の逆行列を求めよ。

$$
A=
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
2 & 3 & 1
\end{pmatrix}
$$

4. 掃き出し法が3次以上の逆行列に使える理由を一言で答えよ。

5. 左側を単位行列にできないとき、逆行列は存在するか答えよ。

### 解答

1.

$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

2.

$$
A^{-1}
=
\begin{pmatrix}
1 & 0 & 0 \\
3 & 1 & 0 \\
9 & 3 & 1
\end{pmatrix}
$$

3.

$$
A^{-1}
=
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & -3 & 1
\end{pmatrix}
$$

4. 行基本操作で左側を単位行列にすれば、右側に逆行列が出るから。
5. 存在しない。

---

## Method 4：階数rankを理解する

### 問題

1. 階数rankとは何か答えよ。

2. 次の行列のrankを答えよ。

$$
\begin{pmatrix}
1 & 2 \\
0 & 3
\end{pmatrix}
$$

3. 次の行列のrankを答えよ。

$$
\begin{pmatrix}
1 & 4 \\
0 & 0
\end{pmatrix}
$$

4. 次の行列のrankを答えよ。

$$
\begin{pmatrix}
1 & 0 & 2 \\
0 & 1 & 3 \\
0 & 0 & 0
\end{pmatrix}
$$

5. 階数を求めるだけなら、単位行列まで変形する必要があるか答えよ。

### 解答

1. 掃き出し法で階段状にしたときの、0だけでない行の本数。
2. $2$
3. $1$
4. $2$
5. 必要ない。0でない行の本数が分かればよい。

---

## Method 5：階数を計算する

### 問題

次の行列のrankを求めよ。

1.

$$
A=
\begin{pmatrix}
4 & -3 \\
-8 & 6
\end{pmatrix}
$$

2.

$$
B=
\begin{pmatrix}
1 & 4 \\
2 & 8
\end{pmatrix}
$$

3.

$$
C=
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

4.

$$
D=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 3 \\
0 & 0 & 4
\end{pmatrix}
$$

5.

$$
E=
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
0 & 1 & 1
\end{pmatrix}
$$

### 解答

1. $\operatorname{rank} A=1$
2. $\operatorname{rank} B=1$
3. $\operatorname{rank} C=2$
4. $\operatorname{rank} D=3$
5. $\operatorname{rank} E=2$
