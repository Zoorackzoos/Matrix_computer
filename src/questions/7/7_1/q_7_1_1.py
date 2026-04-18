from src.A_universal_operations.calc_3_like_funcitons.get_dot_product import get_dot_product


def q_7_1_1(tab_amount = "\t"):
    x = \
        [
            [-5],
            [-2],
            [0]
        ]
    y = \
        [
            [-3],
            [5],
            [-3]
        ]
    tab_amount = "\t"
    variable_lol = get_dot_product(matrix_a=x, matrix_b=y, tab_amount=tab_amount)
    print(variable_lol)


if __name__ == "__main__":
    tab_amount = "\t"
    q_7_1_1(tab_amount = tab_amount)