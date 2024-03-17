from typing import List, Tuple
import random

from utils import generate_random_matrix, generate_random_vector,solve_backwards_substitution, print_matrix, MATRIX_SIZE
# Back substitution: https://www.codesansar.com/numerical-methods/gauss-elimination-method-pseudocode.htm
# Gaus (1 on diagonal): https://pre-epodreczniki.open.agh.edu.pl/tiki-index.php?page=Gaussian+elimination+algorithm


def gauss_elimination(A: List[List[int]], b: List[int]) -> Tuple[List[List[int]], List[int]]:
    N = len(A)
    for irow in range(N):  # loop through rows
        for icol in range(irow + 1, N):  # row scaling
            if A[irow][irow] == 0:
                raise ValueError("Zero on diagonal. Pivoting needed!")
            A[irow][icol] = A[irow][icol] / A[irow][irow]
        b[irow] = b[irow] / A[irow][irow]
        A[irow][irow] = 1.0
        for irow2 in range(irow + 1, N):  # row subtractions
            m = A[irow2][irow]
            for icol in range(irow + 1, N):
                A[irow2][icol] = A[irow2][icol] - m * A[irow][icol]
            b[irow2] = b[irow2] - m * b[irow]
            A[irow2][irow] = 0

    return A, b
if __name__ == "__main__":
    random.seed(2137)
    A = generate_random_matrix(MATRIX_SIZE, MATRIX_SIZE)
    b = generate_random_vector(MATRIX_SIZE)
    print("A matrix:")
    print_matrix(A)
    print("b vector:")
    print_matrix(b)
    A, b = gauss_elimination(A, b)
    print("A gauss:")
    print_matrix(A)
    print("b gauss:")
    print_matrix(b)
    print("Solution for AX = b")
    x = solve_backwards_substitution(A, b)
    print_matrix(x)
