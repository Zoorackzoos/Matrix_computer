from src.operation_functions import *
from src.print_matrix import *

def q_2_4_7(tab_amount="\t"):
    print(tab_amount,"q_2_4_7")
    tab_amount += "\t"
    matrix_in_question = \
        [
            [2,-3,1,"|",0],
            [-2,0,0,"|",0],
            [1,-3,4,"|",0]
        ]
    print_matrix(matrix=matrix_in_question)
    # make it reduced row echalon form ig
    swap_rows(matrix=matrix_in_question,row_1=1,row_2=0)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1/2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=-1/3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)

if __name__ == "__main__":
    q_2_4_7(tab_amount="")