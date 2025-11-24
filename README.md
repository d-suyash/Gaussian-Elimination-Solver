# Gaussian-Elimination-Solver
Python project to solve linear equations using Gauss-Jordan elimination
This program solves a system of linear equations using the Gauss–Jordan elimination method.

The user enters the number of variables and the augmented matrix, and the program reduces it to Reduced Row Echelon Form (RREF) to compute the solution.

#Features

Takes user-defined number of variables (rows).

Automatically calculates the required number of columns (rows + 1).

Accepts input for the augmented matrix.

Handles invalid numerical input.

Performs Gauss–Jordan elimination step by step.

Swaps rows automatically if a pivot becomes zero.

Displays:

Original matrix

Reduced matrix (RREF)

Final solution for each variable

#How It Works

Matrix Input
The program asks:

Enter rows:

Then automatically sets:

columns = rows + 1

The user enters all matrix entries one by one.

Gauss–Jordan Reduction
Each row is normalized so pivot = 1

Non-pivot rows are eliminated

If a pivot position has 0, a row swap is performed

#Solution Output
Example:

x1 = 2.0000

x2 = -1.5000

x3 = 4.2500

#Mathematical Method

The algorithm converts matrix A | b to:

1 0 0 | x1

0 1 0 | x2

0 0 1 | x3

This is known as Reduced Row Echelon Form (RREF).

#Running the Program

Make sure Python and NumPy are installed.

Install NumPy

pip install numpy

Run the script

python gauss_jordan.py

Example Input

Enter rows: 2

You will have 2 rows and 3 columns...

Enter the matrix values:

A[0][0]:1

A[0][1]: 2

A[0][2]: 5

A[1][0]: 3

A[1][1]: 4

A[1][2]: 6
