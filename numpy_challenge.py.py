from math import sqrt
import numpy as np

array_1 = np.array([1, 2, 3, 4])
array_2 = np.diag([22, 22, 22])
array_3 = np.arange(12)
print(array_1)
print(array_2)
print(array_3)

def matrix_multiplication(m1, m2):
    return(np.matmul(m1, m2))


def  multiplication_check(m1, m2):
    try:
        if np.size(m1, 1) == np.size(m2, 0):
            return True
        else:
            return False
    except IndexError:
        if np.size(m1) == np.size(m2):
            return True
        else:
            return False


def multiply_matrices(m1, m2):
    try:
        np.matmul(m1, m2)
        return(np.matmul(m1, m2))
    except ValueError:
        return None


def compute_2d_distance(v1, v2):
    return(sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2))


def compute_multidimensional_distance(v1, v2):
    sum_q = 0
    for i in range(0, len(v1)-1):
        sum_q = sum_q + (v1[i] - v2[i])**2
    return(sqrt(sum_q))


def compute_pair_distances(m):
    size = np.size(m, 1)
    m1 = np.zeros((size, size))
    for i in range(0, size-1):
        for j in range(0, size-1):
            m1[i][j] = compute_multidimensional_distance(m[i], m[j])
    return(m1)
