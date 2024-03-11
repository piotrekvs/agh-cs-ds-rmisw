from typing import List


def multiply_basic(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise Exception("Err: col(A) must be equal to row(B)\n")

    result = [[0] * cols_B for _ in range(rows_A)]

    for row in range(rows_A):
        for col in range(cols_B):
            for i in range(rows_A):
                result[row][col] += A[row][i] * B[i][col]

    return result
