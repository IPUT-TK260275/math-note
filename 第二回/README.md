

## 1. 行列式とは

2次正方行列

$$
A = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

の行列式は、次のように書きます。

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

です。

覚え方は、

$$
\text{左上} \times \text{右下} - \text{右上} \times \text{左下}
$$

です。

---

## 2. 行列式の例

### 例1

$$
|8| = 8
$$

1つだけの数の行列式は、その数そのものです。

### 例2

$$
|-2| = -2
$$

これも同じで、その数そのものになります。

### 例3

$$
\begin{vmatrix}
5 & -6 \\
7 & -8
\end{vmatrix}
$$

$$
= 5 \times (-8) - 7 \times (-6)
$$

$$
= -40 - (-42)
$$

$$
= 2
$$

---

## 3. 練習：行列式を求める

### 問題1

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

$$
= 3 \times 1 - 4 \times 2
$$

$$
= 3 - 8
$$

$$
= -5
$$

### 問題3

$$
\begin{vmatrix}
-2 & 0 \\
7 & 5
\end{vmatrix}
$$

$$
= (-2) \times 5 - 0 \times 7
$$

$$
= -10 - 0
$$

$$
= -10
$$

---

## 4. 行列式の例題

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の行列式を求めます。

$$
\det A =
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix}
$$

$$
= 1 \times 4 - 3 \times 2
$$

$$
= 4 - 6
$$

$$
= -2
$$

---

## 5. 行列のかけ算は順番が大事

行列のかけ算では、ふつうの数と違って、順番を変えると結果が変わることがあります。

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
\quad
B =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
$$

とします。

### AB

$$
AB =
\begin{pmatrix}
4 & 0 \\
-3 & 1
\end{pmatrix}
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
=
\begin{pmatrix}
4 & 0 \\
-3 & 2
\end{pmatrix}
$$

### BA

$$
BA =
\begin{pmatrix}
1 & 0 \\
0 & 2
\end{pmatrix}
\begin{pmatrix}
4 & 0 \\
-3 & 1
\end{pmatrix}
=
\begin{pmatrix}
4 & 0 \\
-6 & 2
\end{pmatrix}
$$

よって、

$$
AB \ne BA
$$

です。

---

## 6. 逆行列とは

行列にも、数でいう「逆数」のようなものがあります。  
それを **逆行列** といいます。

行列 $A$ に対して、

$$
AA^{-1} = E
$$

かつ

$$
A^{-1}A = E
$$

となる行列 $A^{-1}$ を、**Aの逆行列** といいます。

ここで $E$ は単位行列です。

$$
E =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

単位行列は、数でいう $1$ のような役割をします。

---

## 7. 2次正方行列の逆行列の公式

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

のとき、逆行列は次の公式で求められます。

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

のときだけ逆行列が存在します。

---

## 8. 逆行列を求める例題

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

の逆行列を求めます。

まず行列式を求めます。

$$
\det A =
\begin{vmatrix}
1 & 2 \\
3 & 4
\end{vmatrix}
$$

$$
= 1 \times 4 - 3 \times 2
$$

$$
= 4 - 6
$$

$$
= -2
$$

次に公式に当てはめます。

$$
A^{-1}
= \frac{1}{\det A}
\begin{pmatrix}
4 & -2 \\
-3 & 1
\end{pmatrix}
$$

$$
= \frac{1}{-2}
\begin{pmatrix}
4 & -2 \\
-3 & 1
\end{pmatrix}
$$

$$
= \frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
$$

よって、

$$
A^{-1}
=
\begin{pmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{pmatrix}
$$

です。

---

## 9. 逆行列の確かめ

本当に逆行列になっているかは、かけ算して単位行列になるかで確かめます。

$$
AA^{-1} = E
$$

$$
A^{-1}A = E
$$

の両方が成り立てばOKです。

### $AA^{-1}$ の確認

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\quad
A^{-1}
= \frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
$$

$$
AA^{-1}
=
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\cdot
\frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
$$

$$
= \frac{1}{2}
\begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix}
$$

$$
=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
= E
$$

### $A^{-1}A$ の確認

$$
A^{-1}A
= \frac{1}{2}
\begin{pmatrix}
-4 & 2 \\
3 & -1
\end{pmatrix}
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

$$
= \frac{1}{2}
\begin{pmatrix}
2 & 0 \\
0 & 2
\end{pmatrix}
$$

$$
=
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

$$
= E
$$

---

## 10. 逆行列の例題B

$$
B =
\begin{pmatrix}
5 & 3 \\
1 & -1
\end{pmatrix}
$$

の逆行列を求めます。

まず行列式を求めます。

$$
\det B =
\begin{vmatrix}
5 & 3 \\
1 & -1
\end{vmatrix}
$$

$$
= 5 \times (-1) - 1 \times 3
$$

$$
= -5 - 3
$$

$$
= -8
$$

公式に当てはめます。

$$
B^{-1}
= \frac{1}{\det B}
\begin{pmatrix}
-1 & -3 \\
-1 & 5
\end{pmatrix}
$$

$$
= \frac{1}{-8}
\begin{pmatrix}
-1 & -3 \\
-1 & 5
\end{pmatrix}
$$

$$
= \frac{1}{8}
\begin{pmatrix}
1 & 3 \\
1 & -5
\end{pmatrix}
$$

よって、

$$
B^{-1}
= \frac{1}{8}
\begin{pmatrix}
1 & 3 \\
1 & -5
\end{pmatrix}
$$

です。

---

## 11. 逆行列が存在しない場合

$$
C =
\begin{pmatrix}
1 & -1 \\
-3 & 3
\end{pmatrix}
$$

の逆行列を考えます。

まず行列式を求めます。

$$
\det C =
\begin{vmatrix}
1 & -1 \\
-3 & 3
\end{vmatrix}
$$

$$
= 1 \times 3 - (-1) \times (-3)
$$

$$
= 3 - 3
$$

$$
= 0
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

となりますが、今回は

$$
\det C = 0
$$

です。

つまり、

$$
\frac{1}{0}
$$

が出てきてしまいます。  
これは計算できません。

よって、

$$
C^{-1}\ \text{は存在しない}
$$

です。

---

## 12. 逆行列が存在する条件

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

です。

つまり、行列式が0でなければ逆行列は存在します。  
反対に、行列式が0なら逆行列は存在しません。