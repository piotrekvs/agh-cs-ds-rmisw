from typing import List, Tuple
import random

from utils import generate_random_matrix, generate_random_vector, print_matrix, matrix_multiply, \
    solve_backwards_substitution, solve_forwards_substitution, MATRIX_SIZE
# https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html

def LU_decomposition_pivoting(A: List[int]) -> Tuple[List[List[int]], List[List[int]], List[List[int]]]:
    """ Compute the L,U and P matrices from A matrix """
    # Get the number of rows
    n = len(A)

    # Allocate space for P, L, and U
    U = [row[:] for row in A]  # Copy of A
    L = [[0.0] * n for _ in range(n)]
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0
        P[i][i] = 1.0

    # Loop over rows
    for i in range(n):
        # Permute rows if needed
        for k in range(i, n):
            if U[i][i] != 0.0:
                break
            U[k], U[k + 1] = U[k + 1], U[k]
            P[k], P[k + 1] = P[k + 1], P[k]

        # Eliminate entries below i with row operations on U
        # and reverse the row operations to manipulate L
        for j in range(i + 1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return P, L, U


def plu_solve(A, b):
    """ Solve AX = b using P L U decomposition (LU with pivoting)"""
    P, L, U = LU_decomposition_pivoting(A)

    y = solve_forwards_substitution(L, matrix_multiply(P, b))

    return solve_backwards_substitution(U, y)


if __name__ == "__main__":
    random.seed(629)
    A = generate_random_matrix(MATRIX_SIZE, MATRIX_SIZE)
    b = generate_random_vector(MATRIX_SIZE)
    print("A matrix:")
    print_matrix(A)
    print("b vector:")
    print_matrix(b)
    P, L, U = LU_decomposition_pivoting(A)
    print("U matrix:")
    print_matrix(U)
    print("L matrix:")
    print_matrix(L)
    print("P matrix:")
    print_matrix(P)
    print("Solution of AX = b")
    print(plu_solve(A, b))
