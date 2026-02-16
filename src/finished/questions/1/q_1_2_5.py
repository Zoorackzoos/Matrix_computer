from src.finished.print_matrix import *
from src.finished.operation_functions import *

def q_1_2_5(tab_amount="\t"):
    print(tab_amount,"q_1_2_5")
    tab_amount += "\t"
    question_matrix = \
    [
        [-3,6,6,"|",-3],
        [9,-4,0,"|",14],
        [3,1,-4,"|",4]
    ]
    print_matrix(matrix=question_matrix)
    print(tab_amount,"this isn't actually the matrix, the 1 in row 2 is actually a k.")
    print(tab_amount,"For the following system to be consistent,")
    scale_row_from_number(matrix=question_matrix,row_in_question=0,number=-3,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=question_matrix,row_in_question=2,number=3,tab_amount=tab_amount+"\t")
    print_matrix(matrix=question_matrix)
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount+"\t")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount+"\t")
    print_matrix(matrix=question_matrix)
    #r3 <- 2r3 + -3r2
    scale_row_from_number(matrix=question_matrix,row_in_question=2,number=2,tab_amount=tab_amount+"\t")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=1,number=-3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix)