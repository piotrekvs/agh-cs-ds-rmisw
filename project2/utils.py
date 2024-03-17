from typing import List
import random

# Birth date: 04.02.2001 -> matrix size is: 2 + 4 = 6
MATRIX_SIZE = 6

def print_matrix(A: List[List[int]]):
    if not isinstance(A[0], list):  # print vector
        print(A)
        return
    for i in range(len(A)):
        print(A[i])


def generate_random_matrix(rows: int, cols: int) -> List[List[int]]:
    matrix = []
    for _ in range(rows):
        row = [random.randint(0, 10) for _ in range(cols)]
        matrix.append(row)
    return matrix


def generate_random_vector(size: int) -> List[int]:
    return [random.randint(0, 10) for _ in range(size)]


def solve_backwards_substitution(A: List[List[int]], b: List[int]) -> List[int]:
    """
    Solves equation using the backward substitution
    :param A: matrix in format:
    [a, b, c]
    [0, e, f]
    [0, 0, g]
    :param b: vector
    :return: (vector) solution for AX = b
    """
    n = len(b)
    x = [0] * n

    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        xi = b[i]
        for j in range(i + 1, n):
            xi -= A[i][j] * x[j]
        x[i] = xi / A[i][i]  # needed only if not 1s on diagonal

    return x


def solve_forwards_substitution(A: List[List[int]], b: List[int]) -> List[int]:
    """
    Solves equation using the forward substitution
    :param A: matrix in format:
    [a, 0, 0]
    [b, c, 0]
    [d, e, f]
    :param b: vector
    :return: (vector) solution for AX = b
    """
    n = len(A)
    x = [0.0] * n

    # Initializing with the first row.
    x[0] = b[0] / A[0][0]

    # Looping over rows in forward order (from the top down),
    # starting with the second row, because the
    # first row solve is completed in the first step.
    for i in range(1, n):
        sum_val = 0.0
        for j in range(i):
            sum_val += A[i][j] * x[j]
        x[i] = (b[i] - sum_val) / A[i][i]

    return x


def matrix_multiply(A, B):
    """
    :param A: matrix or vector
    :param B: matrix or vector
    :return: matrix or vector
    """
    # Check if A is a vector
    if isinstance(A, (int, float)):
        # A is a vector, convert it to a row matrix
        A = [[elem for elem in A]]

    # Check if B is a vector
    if isinstance(B[0], (int, float)):
        # B is a vector, convert it to a column matrix
        B = [[elem] for elem in B]

    if len(A[0]) != len(B):
        print("Invalid matrix dimensions for multiplication.")
        return None

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    # If A was a vector, return the result as a vector
    if len(A) == 1:
        result = [elem for elem in result[0]]

    # If B was a vector, return the result as a vector
    if len(B[0]) == 1:
        result = [elem[0] for elem in result]

    return result
