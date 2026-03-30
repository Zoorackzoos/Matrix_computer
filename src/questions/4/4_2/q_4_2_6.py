from src.display.print_matrix import print_matrix, print_matrix_frac
from src.matrix_operations.operation_functions import *

def q_4_2_6(tab_amount="\t"):
    matrix_in_question = \
    [
        [-4,4,"|",-3],
        [4,1,"|",-6]
    ]
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=5,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=4,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-1/20,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/20,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question, tab_amount=tab_amount)

if __name__ == "__main__":
    q_4_2_6(tab_amount="")