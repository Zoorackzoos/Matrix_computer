from src.A_universal_operations.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_2_1(tab_amount ="\t"):
    """
    -5 + -4x + -5x^2
    -3 + -3x + -4x^2
    -4 + -2x + -x^2
    -14 + -10x + -10x^2
    ->
    -5, -4, -5
    -3, -3, -4
    -4, -2, -1
    -14, -10, -10
    ->
    -5, -4, -5 = a(-3, -3, -4) + b(-4,-2,-1) + c(-14, -10, -10)
    ->
    -3	-4	-14	|	-5
    -3	-2	-10	|	-4
    -4	-1	-10	|	-5
        row reduce jackass


    :param tab_amount:
    :return:
    """
    matrix_in_question = \
    [
        [-3,-4,-14,"|",-5],
        [-3,-2,-10,"|",-4],
        [-4,-1,-10,"|",-5]
    ]
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=4)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=3)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=13,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=2,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question)




if __name__ == "__main__":
    q_4_2_1()