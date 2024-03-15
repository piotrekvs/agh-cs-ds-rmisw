from typing import List


def multiply_strassen(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_A or cols_A != rows_B or cols_A != cols_B:
        raise Exception("Err: matrices should be squared and of the same size\n")
    
    return multiply_strassen_recurrent(A, B)

def add_matrix(A: List[List[int]], B:  List[List[int]]) -> List[List[int]]:
    return [[A[y][x] + B[y][x] for x in range(len(A[0]))] for y in range(len(A))] 

def subtract_matrix(A: List[List[int]], B:  List[List[int]]) -> List[List[int]]:
    return [[A[y][x] - B[y][x] for x in range(len(A[0]))] for y in range(len(A))] 

def multiply_strassen_recurrent(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    l = len(A)
    C = [[0 for _ in range(l)] for _ in range(l)] 
    
    if (l == 1): 
        C[0][0] = A[0][0] * B[0][0] 
        return C
    
    mid_idx = l // 2
    A00 = [[A[y][x] for x in range(mid_idx)] for y in range(mid_idx)] 
    A01 = [[A[y][x + mid_idx]  for x in range(mid_idx)] for y in range(mid_idx)] 
    A10 = [[A[mid_idx + y][x]  for x in range(mid_idx)] for y in range(mid_idx)] 
    A11 = [[A[y + mid_idx][x + mid_idx]  for x in range(mid_idx)] for y in range(mid_idx)] 
    B00 = [[B[y][x] for x in range(mid_idx)] for y in range(mid_idx)] 
    B01 = [[B[y][x + mid_idx] for x in range(mid_idx)] for y in range(mid_idx)] 
    B10 = [[B[mid_idx + y][x] for x in range(mid_idx)] for y in range(mid_idx)] 
    B11 = [[B[y + mid_idx][x + mid_idx] for x in range(mid_idx)] for y in range(mid_idx)] 

    P1 = multiply_strassen(add_matrix(A00, A11), add_matrix(B00, B11))
    P2 = multiply_strassen(add_matrix(A10, A11), B00)
    P3 = multiply_strassen(A00, subtract_matrix(B01, B11))
    P4 = multiply_strassen(A11, subtract_matrix(B10, B00))
    P5 = multiply_strassen(add_matrix(A00, A01), B11)
    P6 = multiply_strassen(subtract_matrix(A10, A00), add_matrix(B00, B01))
    P7 = multiply_strassen(subtract_matrix(A01, A11), add_matrix(B10, B11))

    C00 = add_matrix(subtract_matrix(add_matrix(P1, P4), P5), P7)
    C01 = add_matrix(P3, P5)
    C10 = add_matrix(P2, P4)
    C11 = add_matrix(add_matrix(subtract_matrix(P1, P2), P3), P6)

    for i in range(mid_idx): 
        for j in range(mid_idx): 
            C[i][j] = C00[i][j] 
            C[i][j + mid_idx] = C01[i][j] 
            C[mid_idx + i][j] = C10[i][j] 
            C[i + mid_idx][j + mid_idx] = C11[i][j] 
    return C
