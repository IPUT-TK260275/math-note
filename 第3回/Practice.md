# 線形代数 第3回 Practice：行列の積と逆行列で連立方程式を解く

この小テストが一通り解ければ、第3回の内容は満点を狙える。
各Methodは5問ずつ。連立方程式は、行列で表すところから練習すること。

---

## Method 1：行列の積を計算する

### 問題

1. 次の積を公式で表せ。

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
$$

2. 次を計算せよ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\begin{pmatrix}
2 & 0 \\
-1 & 5
\end{pmatrix}
$$

3. 次を計算せよ。

$$
\begin{pmatrix}
0 & 1 \\
-2 & 3
\end{pmatrix}
\begin{pmatrix}
4 & -1 \\
2 & 0
\end{pmatrix}
$$

4. 次を計算せよ。

$$
\begin{pmatrix}
1 & 2 & 0 \\
-1 & 3 & 2
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & 4 \\
5 & -2
\end{pmatrix}
$$

5. 次を計算せよ。

$$
\begin{pmatrix}
2 & -1
\end{pmatrix}
\begin{pmatrix}
3 \\
5
\end{pmatrix}
$$

### 解答

1.

$$
\begin{pmatrix}
ae+bg & af+bh \\
ce+dg & cf+dh
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0 & 10 \\
2 & 20
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
2 & 0 \\
-2 & 2
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
2 & 9 \\
8 & 7
\end{pmatrix}
$$

5.

$$
\begin{pmatrix}
1
\end{pmatrix}
$$

---

## Method 2：積の順番を比べる

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

3. $CD$ と $DC$ を計算せよ。

$$
C =
\begin{pmatrix}
1 & 1 \\
0 & 1
\end{pmatrix},
\qquad
D =
\begin{pmatrix}
1 & 0 \\
2 & 1
\end{pmatrix}
$$

4. $AB=C$ と分かっているとき、いつでも $BA=C$ と書いてよいか答えよ。

5. $A$ が $2 \times 3$ 行列、$B$ が $3 \times 2$ 行列のとき、$AB$ と $BA$ はそれぞれ計算できるか。できるなら大きさも答えよ。

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

3.

$$
CD =
\begin{pmatrix}
3 & 1 \\
2 & 1
\end{pmatrix},
\qquad
DC =
\begin{pmatrix}
1 & 1 \\
2 & 3
\end{pmatrix}
$$

4. 書いてはいけない。行列では一般に $AB \ne BA$ である。
5. どちらも計算できる。$AB$ は $2 \times 2$ 行列、$BA$ は $3 \times 3$ 行列。

---

## Method 3：逆行列を復習する

### 問題

1. 次の行列式を求めよ。

$$
\begin{vmatrix}
1 & 1 \\
3 & -5
\end{vmatrix}
$$

2. 次の逆行列を求めよ。

$$
A =
\begin{pmatrix}
1 & 1 \\
3 & -5
\end{pmatrix}
$$

3. 次の行列式を求めよ。

$$
\begin{vmatrix}
2 & 3 \\
3 & -2
\end{vmatrix}
$$

4. 次の逆行列を求めよ。

$$
A =
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
$$

5. 次の行列に逆行列は存在するか答えよ。

$$
A =
\begin{pmatrix}
1 & -4 \\
2 & -8
\end{pmatrix}
$$

### 解答

1. $-8$

2.

$$
A^{-1} =
\frac{1}{8}
\begin{pmatrix}
5 & 1 \\
3 & -1
\end{pmatrix}
$$

3. $-13$

4.

$$
A^{-1} =
\frac{1}{13}
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
$$

5. $\det A=0$ なので、逆行列は存在しない。

---

## Method 4：連立方程式を行列で表す

### 問題

1. 次の連立方程式を行列で表せ。

$$
\begin{cases}
x+2y=5 \\
3x-y=4
\end{cases}
$$

2. 次の連立方程式を行列で表せ。

$$
\begin{cases}
2x-3y=7 \\
-x+4y=-2
\end{cases}
$$

3. 次の行列の式を、連立方程式で表せ。

$$
\begin{pmatrix}
1 & -2 \\
2 & 1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
0 \\
15
\end{pmatrix}
$$

4. 次の式の係数行列、未知数ベクトル、右辺ベクトルをそれぞれ答えよ。

$$
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
8 \\
-1
\end{pmatrix}
$$

5. $AB=C$ から $B=A^{-1}C$ にするため、両辺に $A^{-1}$ をどちら側からかけるか答えよ。

### 解答

1.

$$
\begin{pmatrix}
1 & 2 \\
3 & -1
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
5 \\
4
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
2 & -3 \\
-1 & 4
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
7 \\
-2
\end{pmatrix}
$$

3.

$$
\begin{cases}
x-2y=0 \\
2x+y=15
\end{cases}
$$

4.

$$
A =
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
x \\
y
\end{pmatrix},
\qquad
C =
\begin{pmatrix}
8 \\
-1
\end{pmatrix}
$$

5. 左側からかける。

$$
A^{-1}AB=A^{-1}C
$$

---

## Method 5：逆行列で連立方程式を解く

### 問題

次の連立方程式を解け。

1.

$$
\begin{cases}
x+y=0 \\
3x-5y=16
\end{cases}
$$

2.

$$
\begin{cases}
x-2y=0 \\
2x+y=15
\end{cases}
$$

3.

$$
\begin{cases}
2x+3y=8 \\
3x-2y=-1
\end{cases}
$$

4.

$$
\begin{cases}
x+2y=7 \\
2x+y=8
\end{cases}
$$

5.

$$
\begin{cases}
3x+y=10 \\
x-y=2
\end{cases}
$$

### 解答

1. $x=2,\ y=-2$
2. $x=6,\ y=3$
3. $x=1,\ y=2$
4. $x=3,\ y=2$
5. $x=3,\ y=1$

---

## Method 6：逆行列を使えない場合を判定する

### 問題

1. 次の連立方程式の係数行列の行列式を求め、解の様子を答えよ。

$$
\begin{cases}
x-4y=2 \\
2x-8y=4
\end{cases}
$$

2. 次の連立方程式の係数行列の行列式を求め、解の様子を答えよ。

$$
\begin{cases}
x-4y=2 \\
2x-8y=5
\end{cases}
$$

3. 次の行列に逆行列は存在するか答えよ。

$$
\begin{pmatrix}
2 & 4 \\
1 & 2
\end{pmatrix}
$$

4. 係数行列 $A$ について $\det A \ne 0$ のとき、2元連立方程式の解は何個あるか答えよ。

5. 次の連立方程式の解の様子を答え、一般形を書け。

$$
\begin{cases}
2x+y=1 \\
4x+2y=2
\end{cases}
$$

### 解答

1. $\det A=0$。2本目は1本目の2倍なので、解は無限にある。$y=t$ とすると $x=2+4t$。
2. $\det A=0$。左辺は2倍なのに右辺が2倍ではないので、解はない。
3. $\det A=0$ なので、逆行列は存在しない。
4. ただ1個の解がある。
5. 解は無限にある。$x=t$ とすると $y=1-2t$。

