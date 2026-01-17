from src.print_matrix import *
from src.operation_functions import *

def q_1_2_5(tab_amount="\t"):
    print(tab_amount,"q_1_2_5")
    tab_amount += "\t"
    question_matrix = \
    [
        [-3,6,6,"|",-3],
        [9,-4,1,"|",14],
        [3,1,-4,"|",4]
    ]
    print_matrix(matrix=question_matrix)
    print(tab_amount,"this isn't actually the matrix, the 1 in row 2 is actually a k.")
    print(tab_amount,"For the following system to be consistent,")
    scale_row_from_number(matrix=question_matrix,row_in_question=0,number=-3,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=question_matrix,row_in_question=2,number=3,tab_amount=tab_amount+"\t")
    print_matrix(matrix=question_matrix)
    #if you want the work for this i encourage you to look elsewhere