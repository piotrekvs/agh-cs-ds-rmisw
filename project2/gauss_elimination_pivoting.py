from typing import List, Tuple
import random
from utils import generate_random_matrix, generate_random_vector, print_matrix, solve_backwards_substitution, MATRIX_SIZE

# pseudocode for gauss with pivoting:
# https://users.wpi.edu/~walker/MA514/HANDOUTS/gaussian_elim.pdf


def gaussian_elimination_with_pivoting(A: List[List[int]], b: List[int]) -> Tuple[List[List[int]], List[int]]:
    n = len(A)

    for i in range(n):
        # Pivoting
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        # elimination
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]
    return A, b


if __name__ == '__main__':
    random.seed(420)
    A = generate_random_matrix(MATRIX_SIZE, MATRIX_SIZE)
    b = generate_random_vector(MATRIX_SIZE)
    print("A matrix:")
    print_matrix(A)
    print("b vector:")
    print_matrix(b)
    A, b = gaussian_elimination_with_pivoting(A, b)
    print("A gauss with pivoting:")
    print_matrix(A)
    print("b gauss with pivoting:")
    print_matrix(b)
    print("Solution for AX = b")
    x = solve_backwards_substitution(A, b)
    print_matrix(x)
