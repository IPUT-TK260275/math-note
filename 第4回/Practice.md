# 線形代数 第4回 Practice：掃き出し法で連立方程式を解く

この小テストが一通り解ければ、第4回の内容は満点を狙える。
各Methodは5問ずつ。掃き出し法では、行基本操作を省略しすぎないこと。

---

## Method 1：逆行列による解き方を復習する

### 問題

1. 次の連立方程式を行列の形で表せ。

$$
\begin{cases}
2x+3y=11 \\
x-y=3
\end{cases}
$$

2. 問題1の係数行列 $A$ の行列式を求めよ。

3. 問題1の係数行列 $A$ の逆行列を求めよ。

4. $B=A^{-1}C$ を計算して、問題1の解を求めよ。

5. $AB=C$ から $B=A^{-1}C$ にするとき、$A^{-1}$ は左右どちらからかけるか答えよ。

### 解答

1.

$$
\begin{pmatrix}
2 & 3 \\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
11 \\
3
\end{pmatrix}
$$

2. $\det A=-5$

3.

$$
A^{-1}
=
\frac{1}{5}
\begin{pmatrix}
1 & 3 \\
1 & -2
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
4 \\
1
\end{pmatrix}
$$

よって、$x=4,\ y=1$。

5. 左からかける。

---

## Method 2：行基本操作を理解する

### 問題

1. 次の行列の1行目と2行目を交換せよ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

2. 次の行列の2行目を2倍せよ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

3. 次の行列で、2行目から1行目の3倍を引け。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

4. 次の行列で、1行目に2行目を足せ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

5. 掃き出し法で使う行基本操作を3つ答えよ。

### 解答

1.

$$
\begin{pmatrix}
3 & 4 \\
1 & 2
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
1 & 2 \\
6 & 8
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
1 & 2 \\
0 & -2
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
4 & 6 \\
3 & 4
\end{pmatrix}
$$

5. 行の交換、行の定数倍、ある行に別の行の定数倍を足す操作。

---

## Method 3：拡大係数行列を作る

### 問題

1. 次の連立方程式の拡大係数行列を書け。

$$
\begin{cases}
x+2y=3 \\
3x-y=2
\end{cases}
$$

2. 次の連立方程式の拡大係数行列を書け。

$$
\begin{cases}
4x-y=2 \\
x+3y=7
\end{cases}
$$

3. 次の拡大係数行列を、連立方程式で表せ。

$$
\left(
\begin{array}{cc|c}
1 & -2 & 5 \\
3 & 1 & 4
\end{array}
\right)
$$

4. 次の拡大係数行列で、縦線の左側と右側はそれぞれ何を表すか答えよ。

$$
\left(
\begin{array}{cc|c}
2 & 1 & 8 \\
1 & -1 & 2
\end{array}
\right)
$$

5. 次の連立方程式の拡大係数行列を書け。

$$
\begin{cases}
x-y-z=1 \\
3x-y+2z=4 \\
x-2y+z=0
\end{cases}
$$

### 解答

1.

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
3 & -1 & 2
\end{array}
\right)
$$

2.

$$
\left(
\begin{array}{cc|c}
4 & -1 & 2 \\
1 & 3 & 7
\end{array}
\right)
$$

3.

$$
\begin{cases}
x-2y=5 \\
3x+y=4
\end{cases}
$$

4. 左側は係数、右側は右辺を表す。

5.

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
3 & -1 & 2 & 4 \\
1 & -2 & 1 & 0
\end{array}
\right)
$$

---

## Method 4：2元連立方程式を掃き出し法で解く

### 問題

次の連立方程式を掃き出し法で解け。

1.

$$
\begin{cases}
x+2y=3 \\
3x-y=2
\end{cases}
$$

2.

$$
\begin{cases}
4x-y=2 \\
x+3y=7
\end{cases}
$$

3.

$$
\begin{cases}
x+y=5 \\
2x-y=1
\end{cases}
$$

4.

$$
\begin{cases}
2x+y=7 \\
x-y=1
\end{cases}
$$

5.

$$
\begin{cases}
x-3y=-5 \\
2x+y=11
\end{cases}
$$

### 解答

1. $x=1,\ y=1$
2. $x=1,\ y=2$
3. $x=2,\ y=3$
4. $x=\frac{8}{3},\ y=\frac{5}{3}$
5. $x=4,\ y=3$

---

## Method 5：3元連立方程式を掃き出し法で解く

### 問題

次の連立方程式を掃き出し法で解け。

1.

$$
\begin{cases}
x-y-z=1 \\
3x-y+2z=4 \\
x-2y+z=0
\end{cases}
$$

2.

$$
\begin{cases}
x+y+z=6 \\
x-y+z=2 \\
2x+y-z=3
\end{cases}
$$

3.

$$
\begin{cases}
x+2y=5 \\
y+z=4 \\
x+z=3
\end{cases}
$$

4. 掃き出し法で左側が次の形になった。解を答えよ。

$$
\left(
\begin{array}{ccc|c}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & -1 \\
0 & 0 & 1 & 5
\end{array}
\right)
$$

5. 掃き出し法では、左側をどのような形にすることを目標にするか答えよ。

### 解答

1. $x=\frac{5}{3},\ y=\frac{7}{9},\ z=-\frac{1}{9}$
2. $x=\frac{5}{3},\ y=2,\ z=\frac{7}{3}$
3. $x=1,\ y=2,\ z=2$
4. $x=2,\ y=-1,\ z=5$
5. 単位行列
