import numpy as np
from src.A_universal_operations.float_to_fraction import float_to_fraction_string

def multiply_matrix_static_two_by_two_both_matrices(matrix_a, matrix_b, tab_amount="\t"):
    """
    i made this very long ago. it has not been tested well.
    i'm not entirely sure it's finished.

    :param tab_amount: this is just an amount of "\t"
    :param matrix_a: matrix of reasonable size
    :param matrix_b: matrix of reasonable size
    :return: a 2x2 matrix of the product of the matrices.
    """
    print(tab_amount,"multiply_matrix_static_two_by_two_both_matrices")
    tab_amount += "\t"
    if len(matrix_a) != 2 or len(matrix_b) != 2 or len(matrix_a[0]) != 2 or len(matrix_b[0]) != 2:
        exit("The matrix you put into this function are not 2x2 matrices. please reinput your matrices")

    return_matrix = np.ones((2, 2), dtype=int)
    return_matrix[0][0] = (matrix_a[0][0] * matrix_b[0][0]) + (matrix_a[0][1] * matrix_b[1][0])
    return_matrix[0][1] = (matrix_a[0][0] * matrix_b[0][1]) + (matrix_a[0][1] * matrix_b[1][1])
    return_matrix[1][0] = (matrix_a[1][0] * matrix_b[0][0]) + (matrix_a[1][1] * matrix_b[1][0])
    return_matrix[1][1] = (matrix_a[1][0] * matrix_b[0][1]) + (matrix_a[1][1] * matrix_b[1][1])
    return return_matrix


def multiply_matrix_universal(matrix_a, matrix_b, tab_amount="\t"):
    """
    Credits to eat.shoe AKA Thomas, for finishing this function.
    it multiplies a 2 matrices of any size.

    :param tab_amount: this is just an amount of "\t"
    :param matrix_a: matrix of reasonable size
    :param matrix_b: matrix of reasonable size
    :return: the product of matrix_a and matrix_b
    """
    print(tab_amount, "multiply_matrix")
    tab_amount += "\t"

    # print_matrix(matrix=matrix_a, tab_amount=tab_amount)
    # print_matrix(matrix=matrix_b, tab_amount=tab_amount)

    matrixA_row_amount = len(matrix_a)
    matrixA_column_amount = len(matrix_a[0])

    matrixB_row_amount = len(matrix_b)
    matrixB_column_amount = len(matrix_b[0])
    # return_matrix = np.ones((matrixA_row_amount, matrixB_column_amount), dtype=int)

    if (matrixA_column_amount != matrixB_row_amount):
        exit("un-acceptable matrix multiplication n and m. exiting")

    print(tab_amount, "acceptable matrix multiplication n and m. continuing.")

    return_matrix_un_normalized = []

    for i in range(matrixA_row_amount):
        return_matrix_un_normalized.append([])
        for j in range(matrixB_column_amount):
            return_matrix_un_normalized[i].append(0)
            for k in range(matrixA_column_amount):
                return_matrix_un_normalized[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return return_matrix_un_normalized

"""
if __name__ == "__main__":
    print("program stated")
    matrix_a = \
        [
            [3, 2],
            [-3, -1],
            [-2, 0]
        ]
    matrix_b = \
        [
            [3, -2],
            [1, 3]
        ]
    result_matrix = multiply_matrix_universal(matrix_a=matrix_a, matrix_b=matrix_b, tab_amount="\t")
    print_matrix(result_matrix)
    print("program ended")
"""

def multiply_column_a_and_column_b(column_a, column_b, tab_amount="\t"):
    """
    these matrices ARE NOT nested. they're lists of numbers only.
    so hlep me if you put in
    [
        [n]
    ]
    i'll find you and kiss you hehe :-3

    :param column_a:
    :param column_b:
    :param tab_amount:
    :return:
    """
    print(tab_amount, "multiply_columns_only")
    tab_amount += "\t"

    results_list = []

    column_a_length = len(column_a)
    column_b_length = len(column_b)

    if(isinstance(column_a[0], list)):
        exit("column_a is a list of lists. not cool bro")

    if (isinstance(column_b[0], list)):
        exit("column_a is a list of lists. not cool bro")

    if(column_a_length != column_b_length):
        print(tab_amount,column_a_length)
        print(tab_amount,column_b_length)
        exit("the length of column_a and column_b are not equal")

    for i in range(column_a_length):
        product = column_a[i] * column_b[i]
        results_list.append(product)

    return results_list

def get_sum_of_column(column,tab_amount="\t"):
    print(tab_amount, "get_sum_of_column")
    tab_amount += "\t"

    sum = 0
    for i in range(len(column)):
        sum += column[i]

    return sum

def multiply_column_and_scaler(column, scaler, tab_amount="\t"):
    print(tab_amount, "multiply_column_and_scaler")
    tab_amount += "\t"

    result_column = []

    for i in range(len(column)):
        result_column.append(column[i] * scaler)

    return result_column

def add_column_a_and_column_b(column_a, column_b, tab_amount="\t"):
    print(tab_amount, "add_column_a_and_column_b")
    tab_amount += "\t"

    added_column = []

    for i in range(len(column_a)):
        added_column.append(float_to_fraction_string(column_a[i] + column_b[i]))

    return added_column