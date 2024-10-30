# Problem

Given a $6 \times 6$ 2D Array, `arr`:

$
\begin{bmatrix}
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
\end{bmatrix}
$

An hourglass in `arr` is a subset of values with indices following this pattern in `arr`'s graphical representation:

$
\begin{matrix}
a & b & c \\
  & d &   \\
e & f & g \\
\end{matrix}
$

There are 16 hourglasses in `arr`. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in `arr`, then print the maximum hourglass sum. The array will always be $6 \times 6$.

## Example

If `arr` is:

$
\begin{bmatrix}
-9 & -9 & -9 & 1 & 1 & 1 \\
0 & -9 & 0 & 4 & 3 & 2 \\
-9 & -9 & -9 & 1 & 2 & 3 \\
0 & 0 & 8 & 6 & 6 & 0 \\
0 & 0 & 0 & -2 & 0 & 0 \\
0 & 0 & 1 & 2 & 4 & 0 \\
\end{bmatrix}
$

The 16 hourglass sums are:
$
\begin{matrix}
-63 & -34 & -9 & 12 \\
-10 & 0 & 28 & 23 \\
-27 & -11 & -2 & 10 \\
9 & 17 & 25 & 18 \\
\end{matrix}
$

The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

$
\begin{matrix}
0 & 4 & 3 \\
  & 1 &   \\
8 & 6 & 6 \\
\end{matrix}
$
