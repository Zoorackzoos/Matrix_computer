from src.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_2_5(tab_amount="\t"):
    """
    the vectors
    v1 = \
    [6,
    -3,
    0]

    v2 = \
    [-5,
    2,
    -6]

    v3 = \
    [19,
    -10,
    k]

    form a basis for R^3 if and only if k != ___

    6	-5	19
    -3	2	-10
    0	-6	k


    :param tab_amount:
    :return:
    """
    matrix_in_question = \
    [
        [6, -5, 19],
        [-3, 2, -10],
        [0, -6, "k"]
    ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-6,tab_amount=tab_amount)
    print_matrix(matrix_in_question)

if __name__ == "__main__":
    q_4_2_5(tab_amount="")