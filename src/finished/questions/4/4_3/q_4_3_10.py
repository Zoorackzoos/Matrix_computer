from src.finished.print_matrix import print_matrix, print_matrix_frac
from src.finished.operation_functions import *

def q_4_3_10(tab_amount = '\t'):
    """
    problem 10
    find the rank of the matrix
    A = \
    [
        [-3,5,-5],
        [0,1,-2],
        [-9,15,-17]
    ]
    rank(A) = _

    rank(A) + nullity(A) = number of columns.
    you need the matrix in RREF
    once it’s in RREF.
    the rank is the number of pivots
    the nullity is the number of free variables.

    you don't have to continue this one. it's just he amount of pivots.
    since we can see there's no dependent row. it's just 3

    :param tab_amount:
    :return:
    """
    matrix_in_question = \
    [
        [-3, 5, -5],
        [0, 1, -2],
        [-9, 15, -17]
    ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)

if __name__ == "__main__":
    q_4_3_10(tab_amount="")