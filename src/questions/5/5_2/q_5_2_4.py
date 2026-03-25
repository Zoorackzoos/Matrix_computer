from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def q_5_2_4_a(tab_amount="\t"):
    matrix_a = \
    [
        [-5,1,11,3],
        [-5,-5,3,3],
        [2,3,-1,4],
        [-5,-1,9,4]
    ]
    scale_row_from_number(matrix=matrix_a,row_in_question=0,number=-1,tab_amount=tab_amount)
    # * -1
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=3,row_to_be_added=0,number=1,tab_amount=tab_amount)

    scale_row_from_number(matrix=matrix_a,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_a,row_in_question=2,number=-5,tab_amount=tab_amount)
    # * -1 * 1/2 * -1/5
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)

    scale_row_from_number(matrix=matrix_a,row_in_question=1,number=-17,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_a,row_in_question=2,number=6,tab_amount=tab_amount)
    # * 1/-17 * 1/6
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)

    scale_row_from_number(matrix=matrix_a,row_in_question=3,number=51,tab_amount=tab_amount)
    # * 1/51
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=3,row_to_be_added=1,number=1,tab_amount=tab_amount)

    scale_row_from_number(matrix=matrix_a,row_in_question=3,number=-1,tab_amount=tab_amount)
    # * -1
    scale_row_from_row_and_number(matrix=matrix_a,row_modified=3,row_to_be_added=2,number=1,tab_amount=tab_amount)

    print_matrix(matrix=matrix_a,tab_amount=tab_amount)

    list_of_fed_values = [-1,1/2,-1/5,1/-17,1/6,1/51,-1,10,102,34,-207]
    find_determinant_based_on_list_of_fed_values(list_of_fed_values=list_of_fed_values,tab_amount=tab_amount)

if __name__ == "__main__":
    q_5_2_4_a(tab_amount="")