from src.display.print_matrix import print_matrix_frac
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def q_5_1_2(tab_amount="\t"):
    matrix_in_question = \
    [
        [2,-4,-8,"|",1,0,0],
        [3,4,3,"|",0,1,0],
        [-7,-4,-5,"|",0,0,1]
    ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=3,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=7,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=6,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=108,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=20,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    list_of_fed_values = [1/3,1/2,1/7,1/6,1/108,1/20,42,2160,-720]
    determinant = find_determinant_based_on_fed_array_values(list_of_fed_values=list_of_fed_values,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/42,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2160,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1/720,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1.5,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1/1.5,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=4,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1/4,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_5_1_2(tab_amount="")