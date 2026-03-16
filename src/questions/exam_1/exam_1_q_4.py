from src.display.print_matrix import print_matrix, print_matrix_frac
from src.matrix_operations.operation_functions import *

def exam_1_q_4(tab_amount="\t"):
    print(tab_amount,"exam_1_q_4")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [2,-1,3,"|",1,0,0],
        [0,4,5,"|",0,1,0],
        [1,2,-2,"|",0,0,1]
    ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=5,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=4,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=53,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=25,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1060,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1325,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=3180,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/2809000,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/1060,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1/4213500,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)

if __name__ == "__main__":
    exam_1_q_4(tab_amount="")