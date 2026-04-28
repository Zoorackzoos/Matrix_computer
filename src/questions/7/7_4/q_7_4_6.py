from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_a_and_matrix_b_universal import \
    multiply_matrix_a_and_matrix_b_universal
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import *


def q_7_4_6(tab_amount="\t"):
    print(tab_amount,"q_7_4_6")
    tab_amount += "\t"
    y = \
        [
            [4],
            [-3],
            [3]
        ]
    u = \
    [
        [-2],
        [4],
        [2]
    ]
    """
    proj_u(y) = y * u ) * u
                /
                u * u 
    """
    prod_y_u = get_dot_product(matrix_a=y, matrix_b=u,tab_amount=tab_amount)
    prod_u_u = get_dot_product(matrix_a=u, matrix_b=u,tab_amount=tab_amount)
    frac_of_two_prods = prod_y_u / prod_u_u
    x1 = multiply_matrix_by_scaler(matrix=u,scaler=frac_of_two_prods)
    # six seven!!!!!!!!!!!!!
    # this is x1
    print(tab_amount,matrix_float_to_fraction_string(matrix=x1,tab_amount=tab_amount))

    # b - a
    # y - u1
    x2 = get_subtraction_result_of_two_matrices(matrix_a=x1,matrix_b=y,tab_amount=tab_amount)
    print(tab_amount,matrix_float_to_fraction_string(x2,tab_amount=tab_amount))

if __name__ == "__main__":
    q_7_4_6()