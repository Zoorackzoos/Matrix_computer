from src.display.print_matrix import *
from src.matrix_operations.check_if_matrix_is_all_zeros import get_if_matrix_is_all_zeros
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def set_matrix_pivots_into_ones(matrix_in_question, tab_amount="\t"):
    """
    sets all of the pivots into ones. this creates verbose and sometimes gross floats in the non pivot rows

    :param matrix_in_question:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"turn_matrix_pivots_into_ones")
    tab_amount += "\t"
    for diagonal_index in range(len(matrix_in_question)):
        if matrix_in_question[diagonal_index][diagonal_index] == 0:
            print(tab_amount,"found a 0 where a pivot should be. i'm going to keep going but that's really bad.")
        else:
            matrix_in_question = scale_row_from_number(matrix=matrix_in_question,row_in_question=diagonal_index,number=1/matrix_in_question[diagonal_index][diagonal_index],tab_amount=tab_amount)
    return matrix_in_question

if __name__ == "__main__":
    matrix_in_question = \
    [
        [11234567,2456567,3789053],
        [44567854,5124580,6965467],
        [7456784,80987653,934566]
    ]
    set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question)
    get_REF(matrix_in_question=matrix_in_question)
    print_matrix(matrix_in_question)
