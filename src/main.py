from operation_functions import scale_row_from_row_and_number
from src.print_matrix import print_matrix, print_matrix_frac
from src.tests import *


def q_1_2_3(tab_amount="\t"):
    print(tab_amount,"q_1_2_3")
    tab_amount += "\t"
    question_matrix = \
    [
        [3,2,4,-1],
        [-1,-2,1,-5],
        [0,3,-2,12]
    ]
    print_matrix(question_matrix, tab_amount)
    print(
            tab_amount,"i must make this into reduced row echelon form. \n",
            tab_amount,"which means that I must make a pivot for each row \n",
            tab_amount,"and above and below the pivots, must be 0. also the \n",
            tab_amount,"pivots themselves must be 1."
    )
    swap_rows(matrix=question_matrix,row_1=1,row_2=2,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=0,number=1/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_number(matrix=question_matrix,row_in_question=0,number=1/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_number(matrix=question_matrix,row_in_question=1,number=1/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=2,row_to_be_added=1,number=4/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_number(matrix=question_matrix,row_in_question=2,number=9,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=question_matrix,row_in_question=2,number=1/13,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=1,row_to_be_added=2,number=2/3,tab_amount=tab_amount+"\t")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=0,row_to_be_added=2,number=-4/3,tab_amount=tab_amount+"\t")
    scale_row_from_row_and_number(matrix=question_matrix,row_modified=0,row_to_be_added=1,number=-2/3,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=question_matrix, tab_amount=tab_amount)

if __name__ == '__main__':
    print("program stated")
    q_1_2_3()
    print("program finished")