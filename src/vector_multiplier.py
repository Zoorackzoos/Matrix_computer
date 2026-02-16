import numpy as np

from src.print_matrix import print_matrix, print_matrix_frac
from src.operation_functions import *

def multiply_matrix(matrixA,matrixB, tab_amount="\t"):
    """

    :param matrixA:
    :param matrixB:
    :return:
    """
    print(tab_amount,"multiply_matrix")
    tab_amount += "\t"

    print_matrix(matrix=matrixA,tab_amount=tab_amount)
    print_matrix(matrix=matrixB,tab_amount=tab_amount)

    matrixA_column_amount = len(matrixA)
    matrixB_row_amount = len(matrixB[0])

    return_matrix = np.ones((2, 2), dtype=int)

    if matrixA_column_amount == matrixB_row_amount:
        print(tab_amount,"acceptable matrix multiplication n and m. continuing.")
        top_left = 0
        top_right = 0
        bottom_left = 0
        bottom_right = 0
        for row in matrixA:
            for column in matrixA:

    else:
        exit("un-acceptable matrix multiplication n and m. exiting")

if __name__ == "__main__":
    print("program stated")
    matrixA = \
    [
        [2,5],
        [-3,-7]
    ]
    matrixB = \
    [
        [-7, -5],
        [3,2]
    ]
    multiply_matrix(matrixA=matrixA,matrixB=matrixB)
    print("program ended")