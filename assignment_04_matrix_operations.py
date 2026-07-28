# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1} (numbers only separated by spaces): ").split()))
                if len(row) != cols:
                    print(f"Error: Enter exactly {cols} numbers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Numbers only. Please try again.")
    return matrix


# Function to display a matrix neatly
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# PART A: Transpose a Matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# PART B: Add Two Matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# PART C: Multiply Two Matrices
def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Error: Matrix multiplication is not possible.")
        return None

    result = []

    for i in range(rows_A):
        row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result
print("\nPART A: Transpose a Matrix")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

transposed = transpose_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transposed)


print("\nPART B: Add Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix 1")
matrix1 = read_matrix(rows, cols)

print("\nEnter Matrix 2")
matrix2 = read_matrix(rows, cols)

sum_matrix = add_matrices(matrix1, matrix2)

print("\nResult of Addition:")
display_matrix(sum_matrix)


print("\nPART C: Multiply Two Matrices")

m = int(input("Enter rows for Matrix A: "))
n = int(input("Enter columns for Matrix A: "))

print("\nEnter Matrix A")
A = read_matrix(m, n)

n2 = int(input("\nEnter rows for Matrix B: "))
p = int(input("Enter columns for Matrix B: "))

if n != n2:
    print("Error: Number of columns in Matrix A must equal number of rows in Matrix B.")
else:
    print("\nEnter Matrix B")
    B = read_matrix(n2, p)

    product = multiply_matrices(A, B)

    if product is not None:
        print("\nResult of Multiplication:")
        display_matrix(product)