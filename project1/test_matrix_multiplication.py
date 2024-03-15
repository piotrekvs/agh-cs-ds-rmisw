# type: ignore
import timeit
from typing import List
from matrix_multiplication_basic import multiply_basic
from matrix_multiplication_strassen import multiply_strassen
import matplotlib.pyplot as plt
from random import randint

def print_matrix(A: List[List[int]]):
    for i in range(len(A)): 
        print(A[i], end = "\n")
    print()


def generate_random_square_matrix(n: int, max: int = 100) -> List[List[int]]:
    return [[randint(-max, max) for _ in range(n)] for _ in range(n)] 

iterations = 9
iteration_list = list(range(0, iterations))

def test():
    basic_times = [0.0] * iterations
    strassen_times = [0.0] * iterations
    for i in iteration_list:
        print(f'iteration = {i}')
        A = generate_random_square_matrix(2**i)
        B = generate_random_square_matrix(2**i)
        
        basic_times[i] = timeit.timeit(lambda: multiply_basic(A, B), number=1)
        strassen_times[i] = timeit.timeit(lambda: multiply_strassen(A, B), number=1)

    print(basic_times)
    print(strassen_times)

    plt.plot(basic_times, color='red', label='Basic')
    plt.plot(strassen_times, color='blue', label='Strassen')
    plt.legend()
    plt.xlabel('Matrix size')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

test()






