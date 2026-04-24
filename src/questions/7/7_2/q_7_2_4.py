from src.A_universal_operations.matrix_operations import matrix_multiplier
from src.A_universal_operations.matrix_operations.matrix_multiplier import multiply_matrix_universal, \
    multiply_column_a_and_column_b, get_sum_of_column, multiply_column_and_scaler, add_column_a_and_column_b
from src.A_universal_operations.matrix_operations.matrix_operation_functions import *

def q_7_2_4(tab_amount="\t"):
    print(tab_amount,"q_7_2_4")
    tab_amount += "\t"

    v = \
    [
        10,
        6,
        -9,
        -8
    ]
    w1 = \
    [
        2,
        2,
        6,
        1
    ]
    w2 = \
    [
        0,
        2,
        3,
        -22
    ]

    """
    (v - c1*u1 - c2*u2) * u1 = 0 
    (v - c1*u1 - c2*u2) * u2 = 0 
    """
    product_v_w1 = (multiply_column_a_and_column_b(column_a=v, column_b=w1, tab_amount=tab_amount))
    product_w1_w1 = (multiply_column_a_and_column_b(column_a=w1, column_b=w1, tab_amount=tab_amount))
    product_w2_w1 = (multiply_column_a_and_column_b(column_a=w2, column_b=w1, tab_amount=tab_amount))
    sum_of_product_v_w1 = get_sum_of_column(column=product_v_w1,tab_amount=tab_amount)
    sum_of_product_w1_w1 = get_sum_of_column(column=product_w1_w1,tab_amount=tab_amount)
    sum_of_product_w2_w1 = get_sum_of_column(column=product_w2_w1,tab_amount=tab_amount)

    #(v - c1*u1 - c2*u2) * u2 = 0
    product_v_w2 = (multiply_column_a_and_column_b(column_a=v, column_b=w2, tab_amount=tab_amount))
    product_w1_w2 = (multiply_column_a_and_column_b(column_a=w1, column_b=w2, tab_amount=tab_amount))
    product_w2_w2 = (multiply_column_a_and_column_b(column_a=w2, column_b=w2, tab_amount=tab_amount))
    sum_of_product_v_w2 = get_sum_of_column(column=product_v_w2,tab_amount=tab_amount)
    sum_of_product_w1_w2 = get_sum_of_column(column=product_w1_w2,tab_amount=tab_amount)
    sum_of_product_w2_w2 = get_sum_of_column(column=product_w2_w2,tab_amount=tab_amount)

    print(tab_amount,sum_of_product_v_w1," + -",sum_of_product_w1_w1,"c1 + -",sum_of_product_w2_w1,"c2 = 0")
    print(tab_amount,sum_of_product_v_w2," + -",sum_of_product_w1_w2,"c1 + -",sum_of_product_w2_w2,"c2 = 0")

    """
    from here you need to make the computer do algebra
    i don't know how to do that bestie
    so here it goes
    
    -30 + -45c1 + 0c2 = 0 
    161 + -0c1 + -497c2 = 0 
    -->
    -45c1 = 30
    -497c2 = -161
    -->
    c1 = -30/45 --> -2/3
    c2 = -161/-497 --> 23/71 
    -->
    da_answer_lol = (w1 * -2/3) + (w2 * 23/71)
    """
    w1_scaled = multiply_column_and_scaler(column=w1, scaler=-2/3,tab_amount=tab_amount)
    w2_scaled = multiply_column_and_scaler(column=w2, scaler=23/71,tab_amount=tab_amount)

    print(w1_scaled)
    print(w2_scaled)

    sum_of_w1_scaled_and_w2_scaled = add_column_a_and_column_b(column_a=w1_scaled,column_b=w2_scaled,tab_amount=tab_amount)
    print(sum_of_w1_scaled_and_w2_scaled)

    return "fuck"

if __name__ == "__main__":
    q_7_2_4()