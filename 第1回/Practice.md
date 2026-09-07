# 線形代数 第1回 Practice：行列の基礎

この小テストが一通り解ければ、第1回の内容は満点を狙える。
各Methodは5問ずつ。計算問題は途中式も書くこと。

---

## Method 1：行列の大きさを読む

### 問題

1. 次の行列の大きさを答えよ。

$$
\begin{pmatrix}
2 & -1 & 0 \\
5 & 3 & 4
\end{pmatrix}
$$

2. 次の行列の大きさを答えよ。

$$
\begin{pmatrix}
1 \\
0 \\
-2
\end{pmatrix}
$$

3. 次の行列は何次正方行列か答えよ。

$$
\begin{pmatrix}
1 & 0 & 2 \\
-1 & 3 & 4 \\
5 & 6 & 7
\end{pmatrix}
$$

4. $2 \times 4$ 行列は、何行何列の行列か答えよ。

5. 次の行列の2行目と3列目をそれぞれ答えよ。

$$
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
$$

### 解答

1. $2 \times 3$ 行列
2. $3 \times 1$ 行列
3. 3次正方行列
4. 2行4列
5. 2行目は $\begin{pmatrix}4 & 5 & 6\end{pmatrix}$、3列目は $\begin{pmatrix}3 \\ 6\end{pmatrix}$

---

## Method 2：成分の場所を読む

次の行列を使う。

$$
A =
\begin{pmatrix}
1 & -2 & 5 \\
0 & 3 & 4 \\
-1 & 7 & 8
\end{pmatrix}
$$

### 問題

1. $A$ の $(1,2)$ 成分を答えよ。
2. $A$ の $(2,1)$ 成分を答えよ。
3. $A$ の $(3,2)$ 成分を答えよ。
4. $A$ の $(3,3)$ 成分を答えよ。
5. 成分 $4$ は、どの場所にあるか答えよ。

### 解答

1. $-2$
2. $0$
3. $7$
4. $8$
5. $(2,3)$ 成分

---

## Method 3：行列の足し算・引き算

### 問題

1. $A+B$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
5 & -1 \\
0 & 2
\end{pmatrix}
$$

2. $A-B$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
5 & -1 \\
0 & 2
\end{pmatrix}
$$

3. $B-A$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
5 & -1 \\
0 & 2
\end{pmatrix}
$$

4. 次の2つの行列は足し算できるか答えよ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\quad
\text{と}
\quad
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
$$

5. 次を計算せよ。

$$
\begin{pmatrix}
2 & -3 & 1 \\
0 & 4 & 5
\end{pmatrix}
+
\begin{pmatrix}
1 & 2 & -1 \\
3 & -4 & 0
\end{pmatrix}
$$

### 解答

1.

$$
\begin{pmatrix}
6 & 1 \\
3 & 6
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
-4 & 3 \\
3 & 2
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
4 & -3 \\
-3 & -2
\end{pmatrix}
$$

4. 大きさが違うので足し算できない。

5.

$$
\begin{pmatrix}
3 & -1 & 0 \\
3 & 0 & 5
\end{pmatrix}
$$

---

## Method 4：定数倍と一次結合

### 問題

1. $3A$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

2. $-2B$ を計算せよ。

$$
B =
\begin{pmatrix}
0 & -1 \\
5 & 2
\end{pmatrix}
$$

3. $2A+B$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
0 & -1 \\
5 & 2
\end{pmatrix}
$$

4. $3B-A$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix},
\qquad
B =
\begin{pmatrix}
0 & -1 \\
5 & 2
\end{pmatrix}
$$

5. 次の行列から共通因数 $3$ を外に出せ。

$$
\begin{pmatrix}
6 & 9 \\
-3 & 12
\end{pmatrix}
$$

### 解答

1.

$$
\begin{pmatrix}
3 & 6 \\
9 & 12
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0 & 2 \\
-10 & -4
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
2 & 3 \\
11 & 10
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
-1 & -5 \\
12 & 2
\end{pmatrix}
$$

5.

$$
3
\begin{pmatrix}
2 & 3 \\
-1 & 4
\end{pmatrix}
$$

---

## Method 5：単位行列とゼロ行列

### 問題

1. 2次の単位行列を書け。
2. 3次のゼロ行列を書け。
3. $A+O$ を計算せよ。

$$
A =
\begin{pmatrix}
2 & -1 \\
4 & 0
\end{pmatrix},
\qquad
O =
\begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
$$

4. $A-A$ を計算せよ。

$$
A =
\begin{pmatrix}
2 & -1 \\
4 & 0
\end{pmatrix}
$$

5. $EA$ を計算せよ。

$$
E =
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix},
\qquad
A =
\begin{pmatrix}
3 & 1 \\
2 & 5
\end{pmatrix}
$$

### 解答

1.

$$
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
2 & -1 \\
4 & 0
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
0 & 0 \\
0 & 0
\end{pmatrix}
$$

5.

$$
\begin{pmatrix}
3 & 1 \\
2 & 5
\end{pmatrix}
$$

---

## Method 6：行列の掛け算ができる条件

### 問題

1. $(2 \times 3)(3 \times 4)$ は計算できるか。できるなら答えの大きさも答えよ。
2. $(3 \times 2)(4 \times 1)$ は計算できるか答えよ。
3. $(1 \times 3)(3 \times 1)$ は計算できるか。できるなら答えの大きさも答えよ。
4. $A$ が $2 \times 2$ 行列、$B$ が $2 \times 3$ 行列のとき、$AB$ と $BA$ はそれぞれ計算できるか答えよ。
5. $(4 \times 3)$ 行列に右から何行何列の行列をかけると、答えが $4 \times 2$ 行列になるか答えよ。

### 解答

1. 計算できる。答えは $2 \times 4$ 行列。
2. 真ん中の数字が $2$ と $4$ で一致しないので計算できない。
3. 計算できる。答えは $1 \times 1$ 行列。
4. $AB$ は計算できて $2 \times 3$ 行列になる。$BA$ は計算できない。
5. $3 \times 2$ 行列

---

## Method 7：行列の掛け算を計算する

### 問題

1. 次を計算せよ。

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
5 & -1
\end{pmatrix}
$$

2. 次を計算せよ。

$$
\begin{pmatrix}
2 & -1 \\
0 & 3
\end{pmatrix}
\begin{pmatrix}
1 & 4 \\
2 & 0
\end{pmatrix}
$$

3. 次を計算せよ。

$$
\begin{pmatrix}
1 & 2 & 3
\end{pmatrix}
\begin{pmatrix}
1 \\
0 \\
-1
\end{pmatrix}
$$

4. 次を計算せよ。

$$
\begin{pmatrix}
1 & 0 & -1 \\
2 & 3 & 1
\end{pmatrix}
\begin{pmatrix}
2 & 1 \\
0 & -2 \\
3 & 4
\end{pmatrix}
$$

5. $A^2$ を計算せよ。

$$
A =
\begin{pmatrix}
1 & 2 \\
0 & 1
\end{pmatrix}
$$

### 解答

1.

$$
\begin{pmatrix}
10 & -1 \\
20 & -1
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
0 & 8 \\
6 & 0
\end{pmatrix}
$$

3.

$$
\begin{pmatrix}
-2
\end{pmatrix}
$$

4.

$$
\begin{pmatrix}
-1 & -3 \\
7 & 0
\end{pmatrix}
$$

5.

$$
A^2 =
\begin{pmatrix}
1 & 4 \\
0 & 1
\end{pmatrix}
$$

---

## Method 8：掛け算の順番と展開に注意する

次の行列を使う。

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

### 問題

1. $AB$ を計算せよ。
2. $BA$ を計算せよ。
3. 今回の $A,B$ について、$AB=BA$ といえるか答えよ。
4. 行列では、$(A+B)(A-B)$ をどのように展開するか答えよ。
5. 今回の $A,B$ について、$(A+B)(A-B)$ を計算せよ。

### 解答

1.

$$
\begin{pmatrix}
4 & 0 \\
-3 & 2
\end{pmatrix}
$$

2.

$$
\begin{pmatrix}
4 & 0 \\
-6 & 2
\end{pmatrix}
$$

3. 左下の成分が違うので、$AB=BA$ とはいえない。

4.

$$
(A+B)(A-B)=A^2-AB+BA-B^2
$$

5.

$$
\begin{pmatrix}
15 & 0 \\
-18 & -3
\end{pmatrix}
$$

