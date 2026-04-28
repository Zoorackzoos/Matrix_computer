from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_a_and_matrix_b_universal import \
    multiply_matrix_a_and_matrix_b_universal
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import *


def get_if_sum_row0_row_1_equal_row3(matrix,tab_amount="\t"):
    """
    has to be a matrix that looks like this:
    [
        [x],
        [y],
        [z]
    ]

    :param matrix:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_if_sum_row0_row_1_equal_row3")
    tab_amount += "\t"
    return abs(matrix[0][0] + matrix[1][0]) == abs(matrix[2][0])

def q_7_4_1(tab_amount="\t"):
    print(tab_amount,"q_7_4_1")
    tab_amount += "\t"
    """
    Let W be the set of all vectors
    [
        [x],
        [y],
        [x + y]
    ]
    with x and y real.
    Determine whether each of the following vectors is in W^(vertically_flipped_T)

    *each of these are multiplier choice and are true or false

    :param tab_amount:
    :return:
    """
    v1 = \
        [
            [-5],
            [-5],
            [5]
        ]
    v2 = \
        [
            [-8],
            [9],
            [6]
        ]
    v3 = \
        [
            [2],
            [2],
            [-2]
        ]

    result_1 = get_if_sum_row0_row_1_equal_row3(matrix=v1,tab_amount=tab_amount)
    result_2 = get_if_sum_row0_row_1_equal_row3(matrix=v2,tab_amount=tab_amount)
    result_3 = get_if_sum_row0_row_1_equal_row3(matrix=v3,tab_amount=tab_amount)
    print(result_1)
    print(result_2)
    print(result_3)


if __name__ == "__main__":
    q_7_4_1()