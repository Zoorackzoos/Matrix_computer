from src.A_universal_operations.display.print_matrix import print_matrix
from src.matrix_operations.operation_functions import *

def q_4_2_10_a(tab_amount="\t"):
    matrix_a = \
    [
        [2,-6],
        [-3,9]
    ]
    scale_row_from_number(matrix=matrix_a,row_in_question=0,number=3,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_a,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_a)
    scale_row_from_number(matrix=matrix_a,row_in_question=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_a)

def q_4_2_10_b(tab_amount="\t"):
    matrix_b = \
    [
        [6,-19],
        [-10,30]
    ]
    scale_row_from_number(matrix=matrix_b,row_in_question=0,number=10,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_b,row_in_question=1,number=6,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_b)
    scale_row_from_number(matrix=matrix_b,row_in_question=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_b)
    #scale_row_from_row_and_number(matrix=matrix_b,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    #print_matrix(matrix=matrix_b)

def q_4_2_10_c(tab_amount="\t"):
    matrix_c = \
    [
        [3,3,3],
        [-9,-9,-9],
        [5,5,5]
    ]
    scale_row_from_number(matrix=matrix_c,row_in_question=0,number=-3,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_c)
    scale_row_from_number(matrix=matrix_c,row_in_question=0,number=5,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_c,row_in_question=1,number=5,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_c,row_in_question=2,number=-9,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_c)

def q_4_2_10_d(tab_amount="\t"):
    matrix_d = \
    [
        [1,-1,1],
        [-3,3,-3],
        [2,7,8]
    ]
    scale_row_from_number(matrix=matrix_d,row_in_question=0,number=-3,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_d)
    # probably just 2 but it's whatever.
    scale_row_from_number(matrix=matrix_d,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_d,row_in_question=1,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_d,row_in_question=2,number=-3,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_d)

def q_4_2_10_e(tab_amount="\t"):
    matrix_e = \
    [
        [0,0,0],
        [3,0,0],
        [7,-3,0],
        [1,7,7]
    ]
    scale_row_from_number(matrix=matrix_e,row_in_question=1,number=7,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_e,row_in_question=2,number=3,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_e,row_in_question=3,number=21,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_e)

if __name__ == "__main__":
    q_4_2_10_e(tab_amount="")