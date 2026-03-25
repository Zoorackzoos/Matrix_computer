from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def q_5_2_2(tab_amount = "\t"):
    matrix_in_question = \
    [
        [-2, 2, 5, "|", 1, 0, 0],
        [-3, 0, 2, "|", 0, 1, 0],
        [0, 1, 4, "|", 0, 0, 1]
    ]
    swap_rows(matrix=matrix_in_question,row_1=1,row_2=2,tab_amount=tab_amount)
    # * 1/-1
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=-3)
    # * 1/-3
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=2)
    # * 1/2
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1,tab_amount=tab_amount)
    # * 1/-1
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-6,tab_amount=tab_amount)
    # * 1/-6
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

    list_of_fed_values = [1/-1,1/-3,1/2,1/-1,1/-6,6,-6,-13]
    get_determinant_based_on_list_of_fed_values(list_of_fed_values=list_of_fed_values)

if __name__ == "__main__":
    q_5_2_2(tab_amount="")
