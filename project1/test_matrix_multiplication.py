# type: ignore
import timeit
from matrix_multiplication_strassen import MatrixMultiplier
import matplotlib.pyplot as plt
from random import randint

def print_matrix(A):
    for i in range(len(A)): 
        print(A[i], end = "\n")
    print()


def generate_random_square_matrix(n: int, max: int = 100):
    return [[randint(-max, max) for _ in range(n)] for _ in range(n)] 


mx_multiplier = MatrixMultiplier()

def test_times():
    iterations = 11
    times = [0.0] * iterations
    for i in range(0, iterations):
        print(f'iteration = {i}')
        A = generate_random_square_matrix(2**i)
        B = generate_random_square_matrix(2**i)
        
        times[i] = timeit.timeit(lambda: mx_multiplier.multiply(A, B, 4), number=1)

    plt.plot(times, color='blue')
    plt.legend()
    plt.xlabel('Matrix size (power of 2)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

def test_thresholds():
    thresholds = 9
    times = [0.0] * thresholds

    for i in range(0, thresholds):
        print(f'iteration = {i}')
        A = generate_random_square_matrix(2**8)
        B = generate_random_square_matrix(2**8)
        
        times[i] = timeit.timeit(lambda: mx_multiplier.multiply(A, B, i), number=1)

    plt.plot(times, color='blue')
    plt.legend()
    plt.title("Matrix size 2^8")
    plt.xlabel('Threshold (power of 2)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()


def test_times():
    iterations = 10
    th4 = [0.0] * iterations
    th6 = [0.0] * iterations
    th8 = [0.0] * iterations
    for i in range(0, iterations):
        print(f'iteration = {i}')
        A = generate_random_square_matrix(2**i)
        B = generate_random_square_matrix(2**i)

        mx_multiplier.multiply(A, B, 4)
        th4[i] = mx_multiplier.fp_operations

        mx_multiplier.multiply(A, B, 6)
        th6[i] = mx_multiplier.fp_operations

        mx_multiplier.multiply(A, B, 8)
        th8[i] = mx_multiplier.fp_operations

    plt.plot(th4, color='blue')
    plt.plot(th6, color='green')
    plt.plot(th8, color='red')
    plt.legend()
    plt.xlabel('Matrix size (power of 2)')
    plt.ylabel('Floating point operations')
    plt.show()


def test_multiplication():
    A = generate_random_square_matrix(2**6)
    B = generate_random_square_matrix(2**6)
    C_strassen = mx_multiplier.multiply(A, B, 4)
    C_basic = mx_multiplier.multiply_basic(A, B)
    for row in range(len(C_strassen)):
        for col in range(len(C_strassen)):
            if C_strassen[row][col] != C_basic[row][col]:
                print("error!")
    print("success!")

test_multiplication()






