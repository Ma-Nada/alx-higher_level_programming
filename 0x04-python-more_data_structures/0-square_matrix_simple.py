#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixe = matrix.copy()

    for i in range(len(matrix)):
        matrixe[i] = list(map(lambda x: x**2, matrix[i]))

    return (matrixe)
