import numpy as np

from src.finished.print_matrix import print_matrix


def multiply_matrix_static_two_by_two_both_matrices(matrix_a, matrix_b, tab_amount="\t"):
    """
    :param tab_amount: this is just an amount of "\t"
    :param matrix_a:
    :param matrix_b:
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

    :param tab_amount: this is just an amount of "\t"
    :param matrix_a:
    :param matrix_b:
    :return:
    """
    print(tab_amount,"multiply_matrix")
    tab_amount += "\t"

    print_matrix(matrix=matrix_a, tab_amount=tab_amount)
    print_matrix(matrix=matrix_b, tab_amount=tab_amount)

    matrixA_column_amount = len(matrix_a)
    matrixB_row_amount = len(matrix_b[0])

    return_matrix = np.ones((2, 2), dtype=int)

    if matrixA_column_amount == matrixB_row_amount:
        print(tab_amount,"acceptable matrix multiplication n and m. continuing.")
        return_matrix_un_normalized = []
        #TODO: complete this dog ahh function.
        exit("not finished")
    else:
        exit("un-acceptable matrix multiplication n and m. exiting")

if __name__ == "__main__":
    print("program stated")
    matrix_a = \
    [
        [2,5],
        [-3,-7]
    ]
    matrix_b = \
    [
        [-7, -5],
        [3,2]
    ]
    result_matrix = multiply_matrix_static_two_by_two_both_matrices(matrix_a=matrix_a, matrix_b=matrix_b,tab_amount="\t")
    print_matrix(result_matrix)
    print("program ended")