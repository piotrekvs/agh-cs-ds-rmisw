from typing import List


class MatrixMultiplier():
    def __init__(self) -> None:
        self.threshold: int
        self.fp_operations: int

    def multiply(self, A: List[List[int]], B: List[List[int]], threshold_power: int) -> List[List[int]]:
        self.threshold = 2 ** threshold_power
        self.fp_operations = 0
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])

        if cols_A != rows_A or cols_A != rows_B or cols_A != cols_B:
            raise Exception("Err: matrices should be squares and of the same size\n")
        
        return self._multiply_recurrent(A, B)
    
        
    def _multiply_recurrent(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if self.threshold >= len(A):
            self.fp_operations += len(A) ** 3
            return self.multiply_basic(A, B)
        else:
            return self._multiply_strassen_recurrent(A, B)
    

    def _multiply_strassen_recurrent(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
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

        P1 = self._multiply_recurrent(self.add_matrix(A00, A11), self.add_matrix(B00, B11))
        P2 = self._multiply_recurrent(self.add_matrix(A10, A11), B00)
        P3 = self._multiply_recurrent(A00, self.subtract_matrix(B01, B11))
        P4 = self._multiply_recurrent(A11, self.subtract_matrix(B10, B00))
        P5 = self._multiply_recurrent(self.add_matrix(A00, A01), B11)
        P6 = self._multiply_recurrent(self.subtract_matrix(A10, A00), self.add_matrix(B00, B01))
        P7 = self._multiply_recurrent(self.subtract_matrix(A01, A11), self.add_matrix(B10, B11))

        C00 = self.add_matrix(self.subtract_matrix(self.add_matrix(P1, P4), P5), P7)
        C01 = self.add_matrix(P3, P5)
        C10 = self.add_matrix(P2, P4)
        C11 = self.add_matrix(self.add_matrix(self.subtract_matrix(P1, P2), P3), P6)

        for i in range(mid_idx): 
            for j in range(mid_idx): 
                C[i][j] = C00[i][j] 
                C[i][j + mid_idx] = C01[i][j] 
                C[mid_idx + i][j] = C10[i][j] 
                C[i + mid_idx][j + mid_idx] = C11[i][j] 
        return C
    

    def multiply_basic(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])

        if cols_A != rows_B:
            raise Exception("Err: col(A) must be equal to row(B)\n")

        C = [[0] * cols_B for _ in range(rows_A)]

        for row in range(rows_A):
            for col in range(cols_B):
                for i in range(rows_A):
                    C[row][col] += A[row][i] * B[i][col]
        return C
    
    
    def add_matrix(self, A: List[List[int]], B:  List[List[int]]) -> List[List[int]]:
        self.fp_operations += len(A) ** 2
        return [[A[y][x] + B[y][x] for x in range(len(A[0]))] for y in range(len(A))] 


    def subtract_matrix(self, A: List[List[int]], B:  List[List[int]]) -> List[List[int]]:
        self.fp_operations += len(A[0]) * len(A)
        return [[A[y][x] - B[y][x] for x in range(len(A[0]))] for y in range(len(A))] 
