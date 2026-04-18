from src.A_universal_operations.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_3_12(tab_amount = "\t"):
    matrix_in_question = \
        [
            [-6, -3],
            [-4, -2]
        ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-4,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=6,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    #wuh oh.
    # nuh uh keep goind.
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/24,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)

if __name__ == "__main__":
    q_4_3_12(tab_amount = "")