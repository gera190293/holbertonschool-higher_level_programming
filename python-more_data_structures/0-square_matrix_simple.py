#!/usr/bin/python3

def copy_matrix(matrix=[[]]):
    new_matrix = []
    for i in range(len(matrix)):
        sub_matrix = []
        for j in range(len(matrix[i])):
            sub_matrix.append(matrix[i][j])
        new_matrix.append(sub_matrix)
    return new_matrix


def square_matrix_simple(matrix=[]):
    new_matrix = copy_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    return new_matrix
