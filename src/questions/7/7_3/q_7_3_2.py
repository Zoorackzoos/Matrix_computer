from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_a_and_matrix_b_universal import \
    multiply_matrix_a_and_matrix_b_universal
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import *


def q_7_3_2(tab_amount="\t"):
    print(tab_amount,"q_7_3_2")
    tab_amount += "\t"

    A = \
    [
        [1,-6,5],
        [1,-2,-1],
        [2,-2,-5]
    ]
    #Find an orthonormal basis of the column space of A
    c1 = \
    [
        [A[0][0]],
        [A[1][0]],
        [A[2][0]]
    ]
    c2 = \
        [
            [A[0][1]],
            [A[1][1]],
            [A[2][1]]
        ]
    c3 = \
        [
            [A[0][2]],
            [A[1][2]],
            [A[2][2]]
        ]
    c1_magnitude = get_magnitude_of_matrix(matrix=c1,tab_amount=tab_amount)
    print(tab_amount,"float_to_fraction_string --> ",float_to_fraction_string(value=c1_magnitude))

    # u1 = c1 / || c1 ||
    u1 = multiply_matrix_by_scaler(matrix=c1,scaler=1/c1_magnitude,tab_amount=tab_amount)

    # v2 = c2 - (c2 * u1) * u1
    product_c2_u1 = get_dot_product(matrix_a=c2,matrix_b=u1,tab_amount=tab_amount)
    product_c1u1_u1 = multiply_matrix_by_scaler(matrix=u1,scaler=product_c2_u1,tab_amount=tab_amount)
    sum_c2_product_c1u1u1 = get_subtraction_result_of_two_matrices(matrix_a=c2,matrix_b=product_c1u1_u1,tab_amount=tab_amount)
    print(tab_amount,sum_c2_product_c1u1u1)
    print(tab_amount,matrix_float_to_fraction_string(sum_c2_product_c1u1u1,tab_amount=tab_amount))

    #normalize that bih
    v2_normalized = multiply_matrix_by_scaler(matrix=sum_c2_product_c1u1u1,scaler=1/get_magnitude_of_matrix(matrix=sum_c2_product_c1u1u1,tab_amount=tab_amount))
    print(tab_amount,matrix_float_to_fraction_string(matrix=v2_normalized,tab_amount=tab_amount))

    print()
    print()
    print(matrix_float_to_fraction_string(u1))
    print(matrix_float_to_fraction_string(v2_normalized))

if __name__ == "__main__":
    tab_amount = "\t"
    q_7_3_2(tab_amount=tab_amount)