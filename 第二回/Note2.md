# 線形代数 第2回：行列式と逆行列

このノートでは、2次正方行列の **行列式** と **逆行列** を学ぶ。
行列式は、逆行列が存在するかどうかを判断するための重要な量である。

## 目次

1. [授業の目的](#1-授業の目的)
2. [行列式とは](#2-行列式とは)
3. [行列式の例](#3-行列式の例)
4. [練習：行列式を求める](#4-練習行列式を求める)
5. [行列式の例題](#5-行列式の例題)
6. [行列の掛け算は順番が大事](#6-行列の掛け算は順番が大事)
7. [逆行列とは](#7-逆行列とは)
8. [2次正方行列の逆行列の公式](#8-2次正方行列の逆行列の公式)
9. [逆行列を求める例題](#9-逆行列を求める例題)
10. [逆行列の確かめ](#10-逆行列の確かめ)
11. [逆行列の例題B](#11-逆行列の例題b)
12. [逆行列が存在しない場合](#12-逆行列が存在しない場合)
13. [逆行列が存在する条件](#13-逆行列が存在する条件)
14. [ノートの取り方のポイント](#14-ノートの取り方のポイント)
15. [今日の最重要まとめ](#15-今日の最重要まとめ)
16. [復習用ミニ問題](#16-復習用ミニ問題)
17. [この授業で覚える言葉](#17-この授業で覚える言葉)

---

## 1. 授業の目的

今日の目標は、次のことができるようになることである。

- 2次正方行列の行列式を計算できる
- 行列式の記号 $\det A$ と $|A|$ を読める
- 逆行列の意味を説明できる
- 2次正方行列の逆行列を公式で求められる
- 行列式が $0$ のとき逆行列が存在しないことを理解する

---

## 2. 行列式とは

2次正方行列

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

の行列式は、次のように書く。

$$
\det A = |A| =
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
$$

求め方は、

$$
\det A = ad - bc
$$

である。

### 覚え方

$$
\text{左上} \times \text{右下} - \text{右上} \times \text{左下}
$$

---

## 3. 行列式の例

### 例1

$$
|8| = 8
$$

1つだけの数からなる行列の行列式は、その数そのものである。
ここでの $|8|$ は、絶対値ではなく **1次の行列式** を表している。

### 例2

$$
|-2| = -2
$$

これも同じく、1次の行列式なので、その数そのものになる。

### 例3

$$
\begin{vmatrix}
5 & -6 \\
7 & -8
\end{vmatrix}
$$

$$
\begin{aligned}
\begin{vmatrix}
5 & -6 \\
7 & -8
\end{vmatrix}
&= 5 \times (-8) - (-6) \times 7 \\
&= -40 - (-42) \\
&= 2
\end{aligned}
$$

---

## 4. 練習：行列式を求める

### 問題1

$$
|-5|
$$

解答：

$$
|-5| = -5
$$

### 問題2

$$
\begin{vmatrix}
3 & 2 \\
4 & 1
\end{vmatrix}
$$

解答：

$$
\begin{aligned}
\begin{vmatrix}
3 & 2 \\
4 & 1
\end{vmatrix}
&= 3 \times 1 - 2 \times 4 \\
&= 3 - 8 \\
&= -5
\end{aligned}
$$

### 問題3

$$
\begin{vmatrix}
-2 & 0 \\
7 & 5
\end{vmatrix}
$$

解答：

$$
\begin{aligned}
\begin{vmatrix}
-2 & 0 \\
7 & 5
\end{vmatrix}
&= (-2) \times 5 - 0 \times 7 \\
&= -10 - 0 \\
&= -10
\end{aligned}
$$

---

## 5. 行列式の例題

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の行列式を求める。

### 解答

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix} \\
&= 1 \times 4 - 2 \times 3 \\
&= 4 - 6 \\
&= -2
\end{aligned}
$$

---

## 6. 行列の掛け算は順番が大事

行列の掛け算では、普通の数と違って、順番を変えると結果が変わることがある。

$$
AB \ne BA
$$

例として、

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

とする。

### $AB$

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

### $BA$

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

---

## 7. 逆行列とは

行列にも、数でいう「逆数」のようなものがある。
それを **逆行列** という。

行列 $A$ に対して、

$$
AA^{-1} = E
$$

かつ

$$
A^{-1}A = E
$$

となる行列 $A^{-1}$ を、**$A$ の逆行列** という。

ここで $E$ は単位行列である。

$$
E =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

単位行列は、数でいう $1$ のような役割をする。

---

## 8. 2次正方行列の逆行列の公式

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

のとき、逆行列は次の公式で求められる。

$$
A^{-1}
= \frac{1}{\det A}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

ただし、

$$
\det A \ne 0
$$

のときだけ逆行列が存在する。

---

## 9. 逆行列を求める例題

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の逆行列を求める。

### 解答

まず行列式を求める。

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix} \\
&= 1 \times 4 - 2 \times 3 \\
&= 4 - 6 \\
&= -2
\end{aligned}
$$

次に公式に当てはめる。

$$
\begin{aligned}
A^{-1}
&= \frac{1}{\det A}
\begin{pmatrix}
4 & -2 \\
-3 & 1
\end{pmatrix} \\
&= \frac{1}{-2}
\begin{pmatrix}
4 & -2 \\
-3 & 1
\end{pmatrix} \\
&= \frac{1}{2}
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

## 10. 逆行列の確かめ

本当に逆行列になっているかは、掛け算して単位行列になるかで確かめる。

$$
AA^{-1} = E
$$

$$
A^{-1}A = E
$$

の両方が成り立てばよい。

### $AA^{-1}$ の確認

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
A^{-1}
= \frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
$$

$$
\begin{aligned}
AA^{-1}
&=
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\cdot
\frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix} \\
&=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} \\
&= E
\end{aligned}
$$

### $A^{-1}A$ の確認

$$
\begin{aligned}
A^{-1}A
&=
\frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix} \\
&= \frac{1}{2}
\begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix} \\
&=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix} \\
&= E
\end{aligned}
$$

---

## 11. 逆行列の例題B

$$
B =
\begin{pmatrix}
5 & 3 \\
1 & -1
\end{pmatrix}
$$

の逆行列を求める。

### 解答

まず行列式を求める。

$$
\begin{aligned}
\det B
&=
\begin{vmatrix}
5 & 3 \\
1 & -1
\end{vmatrix} \\
&= 5 \times (-1) - 3 \times 1 \\
&= -5 - 3 \\
&= -8
\end{aligned}
$$

公式に当てはめる。

$$
\begin{aligned}
B^{-1}
&= \frac{1}{\det B}
\begin{pmatrix}
-1 & -3 \\
-1 & 5
\end{pmatrix} \\
&= \frac{1}{-8}
\begin{pmatrix}
-1 & -3 \\
-1 & 5
\end{pmatrix} \\
&= \frac{1}{8}
\begin{pmatrix}
1 & 3 \\
1 & -5
\end{pmatrix}
\end{aligned}
$$

したがって、

$$
B^{-1}
= \frac{1}{8}
\begin{pmatrix}
1 & 3 \\
1 & -5
\end{pmatrix}
$$

である。

---

## 12. 逆行列が存在しない場合

$$
C =
\begin{pmatrix}
1 & -1 \\
-3 & 3
\end{pmatrix}
$$

の逆行列を考える。

### 解答

まず行列式を求める。

$$
\begin{aligned}
\det C
&=
\begin{vmatrix}
1 & -1 \\
-3 & 3
\end{vmatrix} \\
&= 1 \times 3 - (-1) \times (-3) \\
&= 3 - 3 \\
&= 0
\end{aligned}
$$

逆行列の公式では、

$$
C^{-1}
= \frac{1}{\det C}
\begin{pmatrix}
3 & 1 \\
3 & 1
\end{pmatrix}
$$

となるが、今回は

$$
\det C = 0
$$

である。

つまり、

$$
\frac{1}{0}
$$

が出てきてしまう。
これは計算できない。

したがって、

$$
C^{-1}\ \text{は存在しない}
$$

---

## 13. 逆行列が存在する条件

2次正方行列

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

に対して、逆行列が存在する条件は、

$$
\det A \ne 0
$$

である。

つまり、行列式が $0$ でなければ逆行列は存在する。
反対に、行列式が $0$ なら逆行列は存在しない。

---

## 14. ノートの取り方のポイント

教授目線では、次の3点が特に重要である。

### 1. 行列式は途中式を書く

特に符号のミスが起こりやすいので、

$$
ad - bc
$$

のどちらが先に来るかを省略せずに書く。

### 2. 逆行列は「行列式を先に確認」する

逆行列の公式に入る前に、必ず

$$
\det A \ne 0
$$

を確認する。
行列式が $0$ の場合、逆行列は存在しない。

### 3. 公式と計算例を分ける

公式は公式として見出しを立て、例題ではその公式をどのように使ったかを順番に書く。
復習時に「覚える部分」と「計算する部分」を区別しやすくなる。

---

## 15. 今日の最重要まとめ

今日の内容で特に大事なのは、次の4つである。

### 1. 2次正方行列の行列式

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

なら、

$$
\det A = ad - bc
$$

である。

### 2. 逆行列の定義

$$
AA^{-1} = E
$$

かつ

$$
A^{-1}A = E
$$

となる $A^{-1}$ を、$A$ の逆行列という。

### 3. 2次正方行列の逆行列の公式

$$
A^{-1}
= \frac{1}{\det A}
\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

### 4. 逆行列が存在する条件

$$
\det A \ne 0
$$

なら逆行列は存在する。

$$
\det A = 0
$$

なら逆行列は存在しない。

---

## 16. 復習用ミニ問題

### 問題1

次の行列式を求めよ。

$$
\begin{vmatrix}
2 & 5 \\
1 & 3
\end{vmatrix}
$$

解答：

$$
\begin{aligned}
\begin{vmatrix}
2 & 5 \\
1 & 3
\end{vmatrix}
&= 2 \times 3 - 5 \times 1 \\
&= 6 - 5 \\
&= 1
\end{aligned}
$$

### 問題2

次の行列の逆行列が存在するか判断せよ。

$$
\begin{pmatrix}
2 & 4 \\
1 & 2
\end{pmatrix}
$$

解答：

$$
\begin{aligned}
\det A
&=
\begin{vmatrix}
2 & 4 \\
1 & 2
\end{vmatrix} \\
&= 2 \times 2 - 4 \times 1 \\
&= 4 - 4 \\
&= 0
\end{aligned}
$$

したがって、逆行列は存在しない。

### 問題3

次の行列の逆行列を求めよ。

$$
A =
\begin{pmatrix}
2 & 1 \\
1 & 1
\end{pmatrix}
$$

解答：

$$
\begin{aligned}
\det A
&= 2 \times 1 - 1 \times 1 \\
&= 1
\end{aligned}
$$

したがって、

$$
A^{-1}
=
\begin{pmatrix}
1 & -1 \\
-1 & 2
\end{pmatrix}
$$

---

## 17. この授業で覚える言葉

| 用語 | 意味 |
| --- | --- |
| 行列式 | 正方行列に対応する数 |
| $\det A$ | 行列 $A$ の行列式 |
| $\|A\|$ | 行列 $A$ の行列式を表す記号 |
| 逆行列 | 掛けると単位行列になる行列 |
| 単位行列 | 数でいう $1$ のような役割をする行列 |
| $\det A \ne 0$ | 逆行列が存在する条件 |
| $\det A = 0$ | 逆行列が存在しない条件 |

---
