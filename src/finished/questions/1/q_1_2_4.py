from src.finished.operation_functions import *
from src.finished.print_matrix import *

def q_1_2_4(tab_amount="\t"):
    print(tab_amount,"q_1_2_4")
    tab_amount += "\t"
    question_matrix = \
    [
        [1,3,1,"|",-4],
        [3,8,6,"|",-16],
        [1,2,4,"|",-8]
    ]
    print_matrix(matrix=question_matrix,tab_amount=tab_amount)
    print(tab_amount,"i need to make this in reduced echelon form")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=1,row_to_be_added=0,number=-3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix,tab_amount=tab_amount)
    print(tab_amount,"oh dear. that's a problem they all lead to the same thing!")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=1,number=-1,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix,tab_amount=tab_amount)
    print(tab_amount,"the 1st time i did this i forgot to get rid of the top of the pivots. don't be like me.")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=0,row_to_be_added=1,number=3,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=question_matrix,row_in_question=1,number=-1,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix,tab_amount=tab_amount)