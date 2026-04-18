from src.A_universal_operations.calc_3_like_funcitons.get_dot_product import get_dot_product


def q_7_1_2(tab_amount="\t"):
    a = \
    [
        [2,0,-4]
    ]
    b = \
    [
        [1,1,-2]
    ]
    c = \
    [
        [4,2,2]
    ]

    product_ab = get_dot_product(matrix_a=a, matrix_b=b, tab_amount=tab_amount)
    product_ac = get_dot_product(matrix_a=a, matrix_b=c, tab_amount=tab_amount)
    product_bc = get_dot_product(matrix_a=b, matrix_b=c, tab_amount=tab_amount)
    print(product_ab)
    print(product_ac)
    print(product_bc)

if __name__ == "__main__":
    q_7_1_2()