from src.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_3_14(tab_amount = "\t"):
    matrix_in_question = \
        [
            [-2, -4, 5],
            [2, 2, -3],
            [0, 0, 0],
            [4, 6, -8]
        ]
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_4_3_14(tab_amount="")