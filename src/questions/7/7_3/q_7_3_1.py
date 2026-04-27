from src.A_universal_operations.get_dot_product import get_dot_product
from src.A_universal_operations.matrix_operations.get_magnitude_of_matrix import get_magnitude_of_matrix
from src.A_universal_operations.matrix_operations.matrix_float_to_fraction import matrix_float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.matrix_operations.multiply_matrix_by_scaler import multiply_matrix_by_scaler


def q_7_3_1(tab_amount = "\t"):
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
    v2 =    y * x
            /
            y * u1 
    """
    product_xy = get_dot_product(matrix_a=y,matrix_b=x,tab_amount=tab_amount)
    print(tab_amount,product_xy)

if __name__ == "__main__":
    tab_amount = "\t"
    q_7_3_1(tab_amount=tab_amount)