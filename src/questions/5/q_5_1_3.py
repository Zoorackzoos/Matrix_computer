from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def q_5_1_3(tab_amount="\t"):
    matrix_in_question = \
    [
        [2,3,0,9],
        [-7,2,0,0],
        [0,-2,0,0],
        [9,-5,6,-3]
    ]
    swap_rows(matrix=matrix_in_question,row_1=3,row_2=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    swap_rows(matrix=matrix_in_question,row_1=3,row_2=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    swap_rows(matrix=matrix_in_question,row_1=3,row_2=0,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    #that's a total of 3 added -1s
    #-1 * -1 * -1
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=9,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=7,tab_amount=tab_amount)
    #1/7 * 1/9
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=17,tab_amount=tab_amount)
    # 1/-2 * 1/17
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=63,tab_amount=tab_amount)
    # 1/2 * 1/63
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=225,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=34,tab_amount=tab_amount)
    # 1/225 * 1/34
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

    list_of_fed_values = [-126,-7650,-84,19278,-1,-1,-1,1/7,1/9,1/-2,1/17,1/2,1/63,1/225,1/34]
    find_determinant_based_on_fed_array_values(list_of_fed_values=list_of_fed_values,tab_amount=tab_amount)

if __name__ == "__main__":
    q_5_1_3(tab_amount="")