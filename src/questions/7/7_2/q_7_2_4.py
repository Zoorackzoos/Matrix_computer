from src.A_universal_operations.matrix_operations import matrix_multiplier
from src.A_universal_operations.matrix_operations.matrix_multiplier import multiply_matrix_universal
from src.A_universal_operations.matrix_operations.matrix_operation_functions import *

def q_7_2_4(tab_amount="\t"):
    print(tab_amount,"q_7_2_4")
    tab_amount += "\t"

    v = \
    [
        [10],
        [6],
        [-9],
        [-8]
    ]
    w1 = \
    [
        [2],
        [2],
        [6],
        [1]
    ]
    w2 = \
    [
        [0],
        [2],
        [3],
        [-22]
    ]

    """
    (v - c1*u1 - c2*u2) * u1 = 0 
    (v - c1*u1 - c2*u2) * u2 = 0 
    """
    product_v_w1 = multiply_matrix_universal(matrix_a=v,matrix_b=w1,tab_amount=tab_amount)
    product_w1_w1 = multiply_matrix_universal(matrix_a=w1,matrix_b=w1,tab_amount=tab_amount)
    product_w2_w1 = multiply_matrix_universal(matrix_a=w2,matrix_b=w1,tab_amount=tab_amount)
    first_equation_result = [product_v_w1, product_w1_w1, product_w2_w1]

    #(v - c1*u1 - c2*u2) * u2 = 0
    product_v_w2 = multiply_matrix_universal(matrix_a=v, matrix_b=w2, tab_amount=tab_amount)
    product_w1_w2 = multiply_matrix_universal(matrix_a=w1, matrix_b=w2, tab_amount=tab_amount)
    product_w2_w2 = multiply_matrix_universal(matrix_a=w2, matrix_b=w2, tab_amount=tab_amount)
    second_equation_results = [product_v_w2, product_w1_w2, product_w2_w2]

    print(first_equation_result)
    print(second_equation_results)
    return "fuck"

if __name__ == "__main__":
    q_7_2_4()