from src.finished.print_matrix import print_matrix, print_matrix_frac
from src.finished.operation_functions import *

def q_3_2_4(tab_amount):
    print(tab_amount,"q_3_2_4")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [3,3,"|",1,0],
        [-2,7,"|",0,1]
    ]
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-3,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount="\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=27,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=6,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/162,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1/162,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question,tab_amount=tab_amount)



if __name__ == "__main__":
    q_3_2_4(tab_amount="")