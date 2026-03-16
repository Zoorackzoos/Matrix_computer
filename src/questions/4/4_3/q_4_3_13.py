from src.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_3_13(tab_amount = "\t"):
    matrix_in_question = \
    [
        [1, -3, -5, -5],
        [0, 1, -3, -5],
        [-1, 0, 14, 20]
    ]
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)


if __name__ == "__main__":
    q_4_3_13(tab_amount="")