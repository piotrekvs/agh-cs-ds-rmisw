from typing import List, Tuple
import random

from utils import generate_random_matrix,vector_difference_norm, generate_random_vector,  print_matrix, solve_forwards_substitution, solve_backwards_substitution, MATRIX_SIZE
# https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html

def LU_decomposition(A: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    """ Compute the L and U matrices from A matrix """
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [row[:] for row in A]  # U = A (kopia macierzy A)

    for i in range(n):
        L[i][i] = 1.0  # Inicjalizacja elementów diagonalnych macierzy L jako 1

    for i in range(n):
        for j in range(i + 1, n):
            L[j][i] = U[j][i] / U[i][i]  # Obliczenie współczynnika lji

            for k in range(i, n):
                U[j][k] -= L[j][i] * U[i][k]  # Modyfikacja j-tego wiersza macierzy U

    return L, U


def lu_solve(A, b):
    """ Solve AX = b using LU decomposition """
    L, U = LU_decomposition(A)

    y = solve_forwards_substitution(L, b)

    return solve_backwards_substitution(U, y)
if __name__ == "__main__":
    random.seed(125)
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
    x = lu_solve(A, b)
    matlab_result = [
    0.4450171821305839,
    0.5567010309278353,
    -1.5601374570446735,
    -0.8316151202749145,
     2.5773195876288661,
     0.0833333333333333]
    print("Matlab result")
    print(matlab_result)
    print("Norm x1 - x2")
    print(vector_difference_norm(x, matlab_result))



