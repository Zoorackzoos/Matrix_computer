from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import *

def q_7_3_1_main(tab_amount ="\t"):
    x = \
        [
            [-8],
            [2],
            [-2],
            [0]
        ]
    y = \
        [
            [-7],
            [1],
            [11],
            [-3]
        ]
    magnitude_of_x = get_magnitude_of_matrix(matrix=x, tab_amount=tab_amount)
    #magnitude_of_y = get_magnitude_of_column(column=y,tab_amount=tab_amount)

    # 6 * sqrt(2)
    print(tab_amount,"magnitude_of_x -->",float_to_fraction_string(magnitude_of_x))
    """
    this should be eqilent to:
        1          [ -8
        /           2
        6 * sqrt(2) -2
                    0 ]
    this is v1
    """
    v1 = multiply_matrix_by_scaler(matrix=x,scaler=1/magnitude_of_x)
    v1_stringified = matrix_float_to_fraction_string(matrix=v1, tab_amount=tab_amount)
    """
     print_matrix
		 ['-38081/40391']
		 ['19601/83160']
		 ['-19601/83160']
		 ['0']
    same thing as gpt's v1. 
    """
    print_matrix(matrix_in_question=v1_stringified,tab_amount=tab_amount)

    """
    v2 = y - proj_v1(y) 
    v2 = y - (y * u_1) * u_1
    """
    product_yu1 = get_dot_product(matrix_a=y,matrix_b=v1,tab_amount=tab_amount)
    print(tab_amount,"product_yu1 -->",float_to_fraction_string(value=product_yu1))

    proj = multiply_matrix_by_scaler(
        matrix=v1,
        scaler=product_yu1
    )

    v2 = get_subtraction_result_of_two_matrices(matrix_a=multiply_matrix_by_scaler(matrix=y,scaler=-1,tab_amount=tab_amount),matrix_b=proj,tab_amount=tab_amount)
    print(tab_amount,"v2 -->",matrix_float_to_fraction_string(matrix=v2,tab_amount=tab_amount))
    magnitude_of_v2 = get_magnitude_of_matrix(matrix=v2, tab_amount=tab_amount)
    u2 = multiply_matrix_by_scaler(v2, 1 / magnitude_of_v2)
    print(tab_amount,"u2 -->",matrix_float_to_fraction_string(u2))

    print()
    print()
    print(matrix_float_to_fraction_string(matrix=v1,tab_amount=tab_amount))
    print(matrix_float_to_fraction_string(matrix=u2,tab_amount=tab_amount))
    results_list = [v1,u2]
    return results_list

def q_7_3_1_alt(tab_amount = "\t"):
    x = \
        [
            [-8],
            [2],
            [-2],
            [0]
        ]
    y = \
        [
            [-7],
            [1],
            [11],
            [-3]
        ]
    """
    1 / ||x|| * x = v1
    
    y * v1 ) * v1 = v2
    //////
    v1 * v1
    """
    #v1 is a matrix. trust me bro
    v1 = multiply_matrix_by_scaler(matrix=x, scaler=(1 / get_magnitude_of_matrix(x,tab_amount=tab_amount)), tab_amount=tab_amount)
    v2 = multiply_matrix_by_scaler(matrix=v1,scaler=(
                                                    get_dot_product(matrix_a=y,matrix_b=v1,tab_amount=tab_amount))
                                                    /
                                                    (get_dot_product(matrix_a=v1,matrix_b=v1,tab_amount=tab_amount))
                                   ,
                                   tab_amount=tab_amount
                                   )
    print(tab_amount,"v1 --> ",v1)
    #this is supposed to be (-1, 0, 4, -1)
    #not (-4, 1, -1, 0)
    print(tab_amount,"v2 --> ",v2)


if __name__ == "__main__":
    tab_amount = "\t"
    q_7_3_1_alt(tab_amount=tab_amount)