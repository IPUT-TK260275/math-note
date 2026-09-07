# 線形代数 第3回：行列の積と逆行列で連立方程式を解く

このノートでは、行列の積、逆行列、そして逆行列を使った連立方程式の解き方を整理する。

## 目次

1. [今回の目標](#1-今回の目標)
2. [行列はなぜ重要か](#2-行列はなぜ重要か)
3. [行列の積](#3-行列の積)
4. [行列の積では順番が大事](#4-行列の積では順番が大事)
5. [逆行列の復習](#5-逆行列の復習)
6. [2次正方行列の逆行列](#6-2次正方行列の逆行列)
7. [逆行列と連立方程式](#7-逆行列と連立方程式)
8. [例題：連立方程式を逆行列で解く](#8-例題連立方程式を逆行列で解く)
9. [解が無限にある場合](#9-解が無限にある場合)
10. [練習問題](#10-練習問題)
11. [今回のまとめ](#11-今回のまとめ)

---

## 1. 今回の目標

今回の目標は、次の1つである。

> 連立方程式を行列で解けるようになろう。

そのために、まず行列の積を確認し、次に逆行列を使って連立方程式を解く流れを学ぶ。

---

## 2. 行列はなぜ重要か

行列は、たくさんの数をまとめて扱うための道具である。

例えば、次のようなものを行列で表せる。

- 連立方程式の係数
- 画像の画素の並び
- 画像処理に使う変換
- 平面や空間の回転、拡大、縮小

画像も、細かく見ると数の集まりとして扱える。したがって、画像を加工することも、行列に対する計算として考えられる。

---

## 3. 行列の積

次の2つの行列を考える。

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

行列の積は、左の行列の「行」と右の行列の「列」をかけ合わせて計算する。

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
=
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh
\end{pmatrix}
$$

### 計算の見方

左上の成分は、左の1行目と右の1列目から作る。

$$
ae + bg
$$

右上の成分は、左の1行目と右の2列目から作る。

$$
af + bh
$$

左下の成分は、左の2行目と右の1列目から作る。

$$
ce + dg
$$

右下の成分は、左の2行目と右の2列目から作る。

$$
cf + dh
$$

### ポイント

行列の積では、計算する順番を覚えることが大切である。

> 左の「行」と右の「列」を対応させて計算する。

---

## 4. 行列の積では順番が大事

普通の数では、かけ算の順番を変えても答えは同じである。

$$
2 \times 3 = 3 \times 2
$$

しかし、行列では一般に順番を変えると答えが変わる。

$$
AB \ne BA
$$

### 例

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

まず、$AB$ を計算する。

$$
\begin{aligned}
AB
&=
\begin{pmatrix}
4 & 0 \\
-3 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix} \\
&=
\begin{pmatrix}
4 & 0 \\
-3 & 2
\end{pmatrix}
\end{aligned}
$$

次に、$BA$ を計算する。

$$
\begin{aligned}
BA
&=
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
\begin{pmatrix}
4 & 0 \\
-3 & 1
\end{pmatrix} \\
&=
\begin{pmatrix}
4 & 0 \\
-6 & 2
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
AB \ne BA
$$

である。

### ポイント

行列の積では、左右の順番を勝手に入れ替えてはいけない。

---

## 5. 逆行列の復習

数では、$a$ に対して

$$
a \cdot \frac{1}{a} = 1
$$

となる $\frac{1}{a}$ を逆数という。

行列にも、逆数のような役割をする行列がある。それを **逆行列** という。

行列 $A$ に対して、

$$
AX = XA = E
$$

となる行列 $X$ があるとき、$X$ を $A$ の逆行列といい、

$$
X = A^{-1}
$$

と書く。

つまり、

$$
AA^{-1} = E,
\qquad
A^{-1}A = E
$$

である。

ここで、$E$ は単位行列である。

$$
E =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

---

## 6. 2次正方行列の逆行列

2次正方行列

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

の行列式は、

$$
\det A = ad - bc
$$

である。

このとき、$\det A \ne 0$ なら、逆行列は次の公式で求められる。

$$
A^{-1}
=
\frac{1}{\det A}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

### 例

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の逆行列を求める。

まず、行列式を求める。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix} \\
&= 1 \times 4 - 3 \times 2 \\
&= 4 - 6 \\
&= -2
\end{aligned}
$$

次に、公式に代入する。

$$
\begin{aligned}
A^{-1}
&=
\frac{1}{-2}
\begin{pmatrix}
4 & -2 \\
-3 & 1
\end{pmatrix} \\
&=
\frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
A^{-1}
=
\begin{pmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{pmatrix}
$$

である。

---

## 7. 逆行列と連立方程式

次の連立方程式を考える。

$$
\begin{cases}
x + y = 0 \\
3x - 5y = 16
\end{cases}
$$

これは、行列を使って次のように書ける。

$$
\begin{pmatrix}
1 & 1 \\
3 & -5
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
0 \\
16
\end{pmatrix}
$$

ここで、

$$
A =
\begin{pmatrix}
1 & 1 \\
3 & -5
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
0 \\
16
\end{pmatrix}
$$

とおくと、

$$
AB = C
$$

と書ける。

両辺に左から $A^{-1}$ をかける。

$$
A^{-1}AB = A^{-1}C
$$

$A^{-1}A = E$ なので、

$$
EB = A^{-1}C
$$

したがって、

$$
B = A^{-1}C
$$

となる。

### ポイント

逆行列を使うと、連立方程式の解を

$$
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
A^{-1}
\begin{pmatrix}
\text{右辺1} \\
\text{右辺2}
\end{pmatrix}
$$

という形で求められる。

---

## 8. 例題：連立方程式を逆行列で解く

次の連立方程式を解く。

$$
\begin{cases}
x + y = 0 \\
3x - 5y = 16
\end{cases}
$$

行列で表すと、

$$
\begin{pmatrix}
1 & 1 \\
3 & -5
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
0 \\
16
\end{pmatrix}
$$

である。

### 1. 逆行列を求める

$$
A =
\begin{pmatrix}
1 & 1 \\
3 & -5
\end{pmatrix}
$$

とする。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & 1 \\
3 & -5
\end{vmatrix} \\
&= 1 \times (-5) - 1 \times 3 \\
&= -5 - 3 \\
&= -8
\end{aligned}
$$

よって、

$$
\begin{aligned}
A^{-1}
&=
\frac{1}{-8}
\begin{pmatrix}
-5 & -1 \\
-3 & 1
\end{pmatrix} \\
&=
\frac{1}{8}
\begin{pmatrix}
5 & 1 \\
3 & -1
\end{pmatrix}
\end{aligned}
$$

### 2. $B = A^{-1}C$ を計算する

$$
\begin{aligned}
B
&=
A^{-1}C \\
&=
\frac{1}{8}
\begin{pmatrix}
5 & 1 \\
3 & -1
\end{pmatrix}
\begin{pmatrix}
0 \\
16
\end{pmatrix} \\
&=
\frac{1}{8}
\begin{pmatrix}
16 \\
-16
\end{pmatrix} \\
&=
\begin{pmatrix}
2 \\
-2
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
2 \\
-2
\end{pmatrix}
$$

より、

$$
x = 2,
\qquad
y = -2
$$

である。

---

## 9. 解が無限にある場合

次の連立方程式を考える。

$$
\begin{cases}
x - 4y = 2 \\
2x - 8y = 4
\end{cases}
$$

2つ目の式は、1つ目の式を2倍しただけである。

$$
2(x - 4y = 2)
\quad\Longrightarrow\quad
2x - 8y = 4
$$

つまり、実質的には式が1本しかない。

この場合、

$$
x - 4y = 2
$$

から、

$$
x = 2 + 4y
$$

となる。

$y$ には好きな値を代入できるので、解は無限にある。

例えば、

$$
y = 0, 1, 2, 3, \ldots
$$

とすると、

$$
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
2 \\
0
\end{pmatrix},
\begin{pmatrix}
6 \\
1
\end{pmatrix},
\begin{pmatrix}
10 \\
2
\end{pmatrix},
\ldots
$$

のように、いくらでも解が出てくる。

### 行列で見ると

この連立方程式は、

$$
\begin{pmatrix}
1 & -4 \\
2 & -8
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
2 \\
4
\end{pmatrix}
$$

と書ける。

係数行列を

$$
A =
\begin{pmatrix}
1 & -4 \\
2 & -8
\end{pmatrix}
$$

とすると、

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & -4 \\
2 & -8
\end{vmatrix} \\
&= 1 \times (-8) - (-4) \times 2 \\
&= -8 - (-8) \\
&= 0
\end{aligned}
$$

したがって、$A^{-1}$ は存在しない。

逆行列の公式を使おうとすると、

$$
\frac{1}{\det A}
=
\frac{1}{0}
$$

が出てくる。これは計算できない。

### ポイント

逆行列を使って解くには、係数行列の行列式が $0$ ではないことが必要である。

$$
\det A \ne 0
$$

なら、逆行列を使って解ける。

$$
\det A = 0
$$

なら、逆行列を使っては解けない。

---

## 10. 練習問題

### 問題1

次の連立方程式を解く。

$$
\begin{cases}
x - 2y = 0 \\
2x + y = 15
\end{cases}
$$

行列で表す。

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

係数行列を

$$
A =
\begin{pmatrix}
1 & -2 \\
2 & 1
\end{pmatrix}
$$

とする。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & -2 \\
2 & 1
\end{vmatrix} \\
&= 1 \times 1 - (-2) \times 2 \\
&= 1 + 4 \\
&= 5
\end{aligned}
$$

したがって、

$$
A^{-1}
=
\frac{1}{5}
\begin{pmatrix}
1 & 2 \\
-2 & 1
\end{pmatrix}
$$

である。

よって、

$$
\begin{aligned}
\begin{pmatrix}
x \\
y
\end{pmatrix}
&=
\frac{1}{5}
\begin{pmatrix}
1 & 2 \\
-2 & 1
\end{pmatrix}
\begin{pmatrix}
0 \\
15
\end{pmatrix} \\
&=
\frac{1}{5}
\begin{pmatrix}
30 \\
15
\end{pmatrix} \\
&=
\begin{pmatrix}
6 \\
3
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
x = 6,
\qquad
y = 3
$$

である。

### 問題2

次の連立方程式を解く。

$$
\begin{cases}
2x + 3y = 8 \\
3x - 2y = -1
\end{cases}
$$

行列で表す。

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

係数行列を

$$
A =
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
$$

とする。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
2 & 3 \\
3 & -2
\end{vmatrix} \\
&= 2 \times (-2) - 3 \times 3 \\
&= -4 - 9 \\
&= -13
\end{aligned}
$$

したがって、

$$
\begin{aligned}
A^{-1}
&=
\frac{1}{-13}
\begin{pmatrix}
-2 & -3 \\
-3 & 2
\end{pmatrix} \\
&=
\frac{1}{13}
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
\end{aligned}
$$

である。

よって、

$$
\begin{aligned}
\begin{pmatrix}
x \\
y
\end{pmatrix}
&=
\frac{1}{13}
\begin{pmatrix}
2 & 3 \\
3 & -2
\end{pmatrix}
\begin{pmatrix}
8 \\
-1
\end{pmatrix} \\
&=
\frac{1}{13}
\begin{pmatrix}
16 - 3 \\
24 + 2
\end{pmatrix} \\
&=
\frac{1}{13}
\begin{pmatrix}
13 \\
26
\end{pmatrix} \\
&=
\begin{pmatrix}
1 \\
2
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
x = 1,
\qquad
y = 2
$$

である。

---

## 11. 今回のまとめ

今回の内容で特に大切なのは、次の5つである。

### 1. 行列の積は「行」と「列」で計算する

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
=
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh
\end{pmatrix}
$$

### 2. 行列の積は順番が大事

一般に、

$$
AB \ne BA
$$

である。

### 3. 逆行列は単位行列を作る行列である

$$
AA^{-1} = E,
\qquad
A^{-1}A = E
$$

### 4. 2次正方行列の逆行列

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

のとき、

$$
A^{-1}
=
\frac{1}{ad - bc}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

ただし、

$$
ad - bc \ne 0
$$

である。

### 5. 連立方程式は行列で解ける

連立方程式を

$$
AB = C
$$

の形にできれば、

$$
B = A^{-1}C
$$

で解を求められる。

ただし、これは $A^{-1}$ が存在する場合に限る。

