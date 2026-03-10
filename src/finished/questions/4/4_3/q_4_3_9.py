from src.finished.print_matrix import print_matrix, print_matrix_frac
from src.finished.operation_functions import *

def q_4_3_9(tab_amount = "\t"):
    """
    find the value of k for which the matrix
    A = \
    [
        [-9,-4,5],
        [-3,5,8],
        [9,2,k]
    ]
    has rank 2
    k = _

    idk
    i’m gonna row reduce it.


    :param tab_amount:
    :return:
    """
    matrix_in_question = \
        [
            [-9, -4, 5],
            [-3, 5, 8],
            [9, 2, 0]
        ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    # idk about htis move
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1/19,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-7,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)

if __name__ == "__main__":
    q_4_3_9(tab_amount = "")