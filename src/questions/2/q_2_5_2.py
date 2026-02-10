from src.print_matrix import print_matrix, print_matrix_frac
from src.operation_functions import *

def q_2_5_2(tab_amount="\t"):
    print(tab_amount,"q_2_5_2")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [-7,7,2],
        [2,9,5]
    ]
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-7,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-1/14,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1/17,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)

if __name__ == "__main__":
    q_2_5_2(tab_amount="")











