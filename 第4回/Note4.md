# 線形代数 第4回：掃き出し法で連立方程式を解く

このノートでは、逆行列の考え方を復習しながら、**掃き出し法** を使って連立方程式を解く方法を学ぶ。
掃き出し法は、行基本操作によって係数行列を単位行列に変形し、右辺から解を読み取る方法である。

## 目次

1. [今回の目標](#1-今回の目標)
2. [逆行列による解き方の復習](#2-逆行列による解き方の復習)
3. [掃き出し法とは](#3-掃き出し法とは)
4. [行基本操作](#4-行基本操作)
5. [拡大係数行列](#5-拡大係数行列)
6. [2元連立方程式を掃き出し法で解く](#6-2元連立方程式を掃き出し法で解く)
7. [3元連立方程式を掃き出し法で解く](#7-3元連立方程式を掃き出し法で解く)
8. [今回のまとめ](#8-今回のまとめ)

---

## 1. 今回の目標

今回の目標は、次のことである。

> 掃き出し法を使った連立方程式の解き方を理解する。

第3回では、逆行列を使って

$$
AB=C
$$

から

$$
B=A^{-1}C
$$

として連立方程式を解いた。

今回の掃き出し法では、逆行列を直接求めなくても、行の操作によって解を求められるようになる。

---

## 2. 逆行列による解き方の復習

次の連立方程式を考える。

$$
\begin{cases}
2x+3y=11 \\
x-y=3
\end{cases}
$$

係数を行列でまとめると、

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

である。

ここで、

$$
A=
\begin{pmatrix}
2 & 3 \\
1 & -1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
x \\
y
\end{pmatrix},
\qquad
C=
\begin{pmatrix}
11 \\
3
\end{pmatrix}
$$

とおくと、

$$
AB=C
$$

と書ける。

両辺に左から $A^{-1}$ をかけると、

$$
A^{-1}AB=A^{-1}C
$$

となる。

$A^{-1}A=E$ なので、

$$
B=A^{-1}C
$$

である。

まず、$A^{-1}$ を求める。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
2 & 3 \\
1 & -1
\end{vmatrix} \\
&=2\times(-1)-3\times1 \\
&=-2-3 \\
&=-5
\end{aligned}
$$

したがって、

$$
\begin{aligned}
A^{-1}
&=
\frac{1}{-5}
\begin{pmatrix}
-1 & -3 \\
-1 & 2
\end{pmatrix} \\
&=
\frac{1}{5}
\begin{pmatrix}
1 & 3 \\
1 & -2
\end{pmatrix}
\end{aligned}
$$

よって、

$$
\begin{aligned}
B
&=
A^{-1}C \\
&=
\frac{1}{5}
\begin{pmatrix}
1 & 3 \\
1 & -2
\end{pmatrix}
\begin{pmatrix}
11 \\
3
\end{pmatrix} \\
&=
\frac{1}{5}
\begin{pmatrix}
20 \\
5
\end{pmatrix} \\
&=
\begin{pmatrix}
4 \\
1
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
x=4,
\qquad
y=1
$$

である。

---

## 3. 掃き出し法とは

掃き出し法とは、行列の **行** に対して操作を行い、左側を単位行列に変形する方法である。

連立方程式を

$$
AB=C
$$

と書いたとき、掃き出し法では

$$
\left(
\begin{array}{cc|c}
2 & 3 & 11 \\
1 & -1 & 3
\end{array}
\right)
$$

のように、係数と右辺を1つにまとめる。

この行列を、行基本操作で

$$
\left(
\begin{array}{cc|c}
1 & 0 & x \\
0 & 1 & y
\end{array}
\right)
$$

の形にできれば、右端から解を読み取れる。

---

## 4. 行基本操作

掃き出し法で使う操作は、主に次の3つである。

### 1. 行を交換する

例えば、

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の1行目と2行目を交換すると、

$$
\begin{pmatrix}
3 & 4 \\
1 & 2
\end{pmatrix}
$$

になる。

### 2. 行を0でない数倍する

例えば、2行目を2倍すると、

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
1 & 2 \\
6 & 8
\end{pmatrix}
$$

になる。

### 3. ある行に、別の行の何倍かを足す

例えば、2行目から1行目の3倍を引くと、

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\longrightarrow
\begin{pmatrix}
1 & 2 \\
0 & -2
\end{pmatrix}
$$

になる。

### ポイント

掃き出し法では、これらの操作を使って、左側を次のような単位行列に近づけていく。

$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

---

## 5. 拡大係数行列

連立方程式の係数と右辺をまとめた行列を **拡大係数行列** という。

例えば、

$$
\begin{cases}
x+2y=3 \\
3x-y=2
\end{cases}
$$

なら、拡大係数行列は

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
3 & -1 & 2
\end{array}
\right)
$$

である。

縦線の左側が係数、右側が右辺を表す。

---

## 6. 2元連立方程式を掃き出し法で解く

次の連立方程式を解く。

$$
\begin{cases}
x+2y=3 \\
3x-y=2
\end{cases}
$$

拡大係数行列にする。

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
3 & -1 & 2
\end{array}
\right)
$$

まず、2行目から1行目の3倍を引く。

$$
R_2 \leftarrow R_2-3R_1
$$

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
0 & -7 & -7
\end{array}
\right)
$$

次に、2行目を $-\frac{1}{7}$ 倍する。

$$
R_2 \leftarrow -\frac{1}{7}R_2
$$

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 1 & 1
\end{array}
\right)
$$

最後に、1行目から2行目の2倍を引く。

$$
R_1 \leftarrow R_1-2R_2
$$

$$
\left(
\begin{array}{cc|c}
1 & 0 & 1 \\
0 & 1 & 1
\end{array}
\right)
$$

したがって、

$$
x=1,
\qquad
y=1
$$

である。

---

## 7. 3元連立方程式を掃き出し法で解く

次の連立方程式を解く。

$$
\begin{cases}
x-y-z=1 \\
3x-y+2z=4 \\
x-2y+z=0
\end{cases}
$$

拡大係数行列にする。

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
3 & -1 & 2 & 4 \\
1 & -2 & 1 & 0
\end{array}
\right)
$$

まず、1列目の下を0にする。

$$
R_2 \leftarrow R_2-3R_1,
\qquad
R_3 \leftarrow R_3-R_1
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
0 & 2 & 5 & 1 \\
0 & -1 & 2 & -1
\end{array}
\right)
$$

2行目を $\frac{1}{2}$ 倍する。

$$
R_2 \leftarrow \frac{1}{2}R_2
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
0 & 1 & \frac{5}{2} & \frac{1}{2} \\
0 & -1 & 2 & -1
\end{array}
\right)
$$

3行目に2行目を足す。

$$
R_3 \leftarrow R_3+R_2
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
0 & 1 & \frac{5}{2} & \frac{1}{2} \\
0 & 0 & \frac{9}{2} & -\frac{1}{2}
\end{array}
\right)
$$

3行目を $\frac{2}{9}$ 倍する。

$$
R_3 \leftarrow \frac{2}{9}R_3
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
0 & 1 & \frac{5}{2} & \frac{1}{2} \\
0 & 0 & 1 & -\frac{1}{9}
\end{array}
\right)
$$

あとは上側の余分な成分を0にする。

$$
R_2 \leftarrow R_2-\frac{5}{2}R_3
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & -1 & 1 \\
0 & 1 & 0 & \frac{7}{9} \\
0 & 0 & 1 & -\frac{1}{9}
\end{array}
\right)
$$

$$
R_1 \leftarrow R_1+R_3
$$

$$
\left(
\begin{array}{ccc|c}
1 & -1 & 0 & \frac{8}{9} \\
0 & 1 & 0 & \frac{7}{9} \\
0 & 0 & 1 & -\frac{1}{9}
\end{array}
\right)
$$

$$
R_1 \leftarrow R_1+R_2
$$

$$
\left(
\begin{array}{ccc|c}
1 & 0 & 0 & \frac{5}{3} \\
0 & 1 & 0 & \frac{7}{9} \\
0 & 0 & 1 & -\frac{1}{9}
\end{array}
\right)
$$

したがって、

$$
x=\frac{5}{3},
\qquad
y=\frac{7}{9},
\qquad
z=-\frac{1}{9}
$$

である。

---

## 8. 今回のまとめ

今回の内容で特に大事なのは、次の5つである。

### 1. 掃き出し法は行基本操作で解く方法

行を交換する、行を定数倍する、行に別の行の定数倍を足す、という操作を使う。

### 2. 連立方程式は拡大係数行列にまとめる

係数と右辺をまとめて、

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3 \\
3 & -1 & 2
\end{array}
\right)
$$

のように書く。

### 3. 左側を単位行列にする

左側が

$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

になれば、右側から解を読み取れる。

### 4. 2元だけでなく3元にも使える

掃き出し法は、2元連立方程式だけでなく、3元以上の連立方程式にも使える。

### 5. 逆行列を直接求めなくても解ける

第3回の逆行列による方法と同じ発想だが、掃き出し法では行操作だけで解を求められる。
