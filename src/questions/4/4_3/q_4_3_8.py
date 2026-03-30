from src.display.print_matrix import print_matrix, print_matrix_frac
from src.matrix_operations.operation_functions import *

def q_4_3_8(tab_amount="\t"):
    """
    Find the rank and nullity of the matrix
    A = \
    [
        [-2, -6, 5, -3, 0],
        [1,4,-7,1,-6],
        [-1,-3,3,-1,1]
    ]
    rank(A) = _
    nullity(A) = _
    rank(A) + nullity(A) = “number of rows” or “number of columns”

    you need the matrix in RREF
    once it’s in RREF.
    the rank is the number of pivots
    the nullity is the number of free variables.

    :param tab_amount:
    :return:
    """
    matrix_in_question = \
        [
            [-2, -6, 5, -3, 0],
            [1, 4, -7, 1, -6],
            [-1, -3, 3, -1, 1]
        ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-2,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-1/2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=9/2,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=5/2,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-3,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1/3,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=2/5,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question)

if __name__ == "__main__":
    q_4_3_8(tab_amount="\t")