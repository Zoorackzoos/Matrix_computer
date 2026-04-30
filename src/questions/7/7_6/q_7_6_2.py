from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.REF_and_RREF_getters import get_REF
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix, print_matrix_frac
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_a_and_matrix_b_universal import \
    multiply_matrix_a_and_matrix_b_universal
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import *
from src.A_universal_operations.matrix_operations.REF_and_RREF_getters.get_REF import *

def q_7_6_2(tab_amount="\t"):
    """
    27	23	|	73
    23	27	|	77
        row reduce bro
    :param tab_amount:
    :return:
    """
    matrix_in_question = \
    [
        [27, 23, "|", 73],
        [23, 27, "|", 77],
    ]
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=27,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-23,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/27,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1/23,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_7_6_2()







