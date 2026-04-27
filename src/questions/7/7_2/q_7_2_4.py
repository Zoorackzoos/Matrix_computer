from src.A_universal_operations.calc_3_like_funcitons.get_magnitude import get_magnitude_of_matrix
from src.A_universal_operations.column_float_to_fraction import column_float_to_fraction_string
from src.A_universal_operations.matrix_operations import matrix_multiplier
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import \
    get_subtraction_result_of_two_matrices
from src.A_universal_operations.matrix_operations.matrix_multiplier import multiply_matrix_a_and_matrix_b_universal, \
    multiply_column_a_and_column_b, get_sum_of_column, multiply_column_and_scaler, add_column_a_and_column_b
from src.A_universal_operations.matrix_operations.matrix_operation_functions import *
from src.A_universal_operations.float_to_fraction import float_to_fraction_string

def q_7_2_4(tab_amount="\t"):
    print(tab_amount,"q_7_2_4")
    tab_amount += "\t"

    y = \
    [
        -4,
        4,
        7
    ]
    u1 = \
    [
        -5,
        -4,
        1
    ]
    u2 = \
    [
        -4,
        -2,
        -28
    ]
    """
    (v - c1*u1 - c2*u2) * u1 = 0 
    (v - c1*u1 - c2*u2) * u2 = 0 
    """
    prod_y_u1 = multiply_column_a_and_column_b(column_a=y, column_b=u1,tab_amount=tab_amount)
    prod_u1_u1 = multiply_column_a_and_column_b(column_a=u1, column_b=u1,tab_amount=tab_amount)
    prod_u2_u1 = multiply_column_a_and_column_b(column_a=u2, column_b=u1,tab_amount=tab_amount)
    sum_of_prod_y_u1 = get_sum_of_column(prod_y_u1)
    sum_of_prod_u1_u1 = get_sum_of_column(prod_u1_u1)
    sum_of_prod_u2_u1 = get_sum_of_column(prod_u2_u1)

    prod_y_u2 = multiply_column_a_and_column_b(column_a=y, column_b=u2,tab_amount=tab_amount)
    prod_u1_u2 = multiply_column_a_and_column_b(column_a=u1, column_b=u2,tab_amount=tab_amount)
    prod_u2_u2 = multiply_column_a_and_column_b(column_a=u2, column_b=u2,tab_amount=tab_amount)
    sum_of_prod_y_u2 = get_sum_of_column(prod_y_u2)
    sum_of_prod_u1_u2 = get_sum_of_column(prod_u1_u2)
    sum_of_prod_u2_u2 = get_sum_of_column(prod_u2_u2)

    print(tab_amount,sum_of_prod_y_u1," + -",sum_of_prod_u1_u1,"c1 + -",sum_of_prod_u2_u1,"c2 = 0")
    print(tab_amount,sum_of_prod_y_u2," + -",sum_of_prod_u1_u2,"c1 + -",sum_of_prod_u2_u2,"c2 = 0")
    """
         11  + - 42 c1 + - 0 c2 = 0
		 -188  + - 0 c1 + - 804 c2 = 0
		 -->
		 11 = 42 * c1
		 -188 = 804 * c2
		 -->
		 11/42 = c1
		 -188/804 --> -47/201 = c2
		 
    """
    scaled_u1 = multiply_column_and_scaler(column=u1,scaler=11/42)
    scaled_u2 = multiply_column_and_scaler(column=u2,scaler=-47/201)

    # this is also called projection. but like who tf cares
    sum_of_scaled_u1_and_scaled_u2 = add_column_a_and_column_b(column_a=scaled_u2, column_b=scaled_u1, tab_amount=tab_amount)
    print()
    print(y)
    print(sum_of_scaled_u1_and_scaled_u2)
    print()
    print(y)
    sum_of_scaled_u1_and_scaled_u2 = multiply_column_and_scaler(column=sum_of_scaled_u1_and_scaled_u2,scaler=-1,tab_amount=tab_amount)
    print(sum_of_scaled_u1_and_scaled_u2)

    some_bullshit = add_column_a_and_column_b(column_a=y, column_b=sum_of_scaled_u1_and_scaled_u2,tab_amount=tab_amount)
    print(tab_amount,some_bullshit)
    magnitude_some_bullshit = get_magnitude_of_matrix(matrix=[some_bullshit], tab_amount=tab_amount)
    print(float_to_fraction_string(magnitude_some_bullshit))

if __name__ == "__main__":
    q_7_2_4()