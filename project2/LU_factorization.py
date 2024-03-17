from typing import List, Tuple
import random

from utils import generate_random_matrix, generate_random_vector,  print_matrix, solve_forwards_substitution, solve_backwards_substitution, MATRIX_SIZE
# https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html

def LU_decomposition(A: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    """ Compute the L and U matrices from A matrix """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1.0

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U


def lu_solve(A, b):
    """ Solve AX = b using LU decomposition """
    L, U = LU_decomposition(A)

    y = solve_forwards_substitution(L, b)

    return solve_backwards_substitution(U, y)
if __name__ == "__main__":
    random.seed(666)
    A = generate_random_matrix(MATRIX_SIZE, MATRIX_SIZE)
    b = generate_random_vector(MATRIX_SIZE)
    print("A matrix:")
    print_matrix(A)
    print("b vector:")
    print_matrix(b)
    L, U = LU_decomposition(A)
    print("U matrix:")
    print_matrix(U)
    print("L matrix:")
    print_matrix(L)
    print("Solution of AX = b")
    print(lu_solve(A, b))



