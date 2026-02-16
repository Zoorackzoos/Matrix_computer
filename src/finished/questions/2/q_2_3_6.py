from src.finished.print_matrix import print_matrix, print_matrix_frac
from src.finished.operation_functions import *

def q_2_3_6_a(tab_amount="\t"):
    print_matrix(tab_amount,"q_2_3_6_a")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [6,8,"|",-64],
        [4,1,"|",-21]
    ]
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=4,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=6,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/24,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/-26,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=-1+-1/3,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

def q_2_3_6_b(tab_amount="\t"):
    print_matrix(tab_amount,"q_2_3_6_b")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [6,8,"|",-20],
        [4,1,"|",-9]
    ]
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=4,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=6,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/24,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/-26,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=-1+-1/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_2_3_6_b()