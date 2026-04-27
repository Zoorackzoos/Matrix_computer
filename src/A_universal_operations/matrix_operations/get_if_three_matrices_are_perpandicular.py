from src.A_universal_operations.calc_3_like_funcitons.get_dot_product import get_dot_product


def get_if_three_matrices_are_perpendicular(matrix_a, matrix_b, matrix_c, tab_amount ="\t"):
    """
    To determine if three vectors are perpendicular to each other (mutually perpendicular),
     you must verify that the dot product of every possible pair is zero. For three vectors

    :param matrix_a:
    :param matrix_b:
    :param matrix_c:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_if_three_matrices_are_perpendicular")
    tab_amount += "\t"

    #ab = get_dot_product(matrix_a=matrix_a, matrix_b=matrix_b,tab_amount=tab_amount)
    ac = get_dot_product(matrix_a=matrix_a, matrix_b=matrix_c,tab_amount=tab_amount)
    bc = get_dot_product(matrix_a=matrix_b, matrix_b=matrix_c,tab_amount=tab_amount)

    return_bool = False

    #visually this looks like a triangle. for it to be perpendicular it has to have a 90 degree angle
    #so the ab doesn't matter :-/
    #ab_equals_zero_bool = ab == 0
    #print(tab_amount,"ab_equals_zero_bool = ",ab_equals_zero_bool)
    ac_equals_zero_bool = ac == 0
    print(tab_amount,"ac_equals_zero_bool = ",ac_equals_zero_bool)
    bc_equals_zero_bool = bc == 0
    print(tab_amount,"bc_equals_zero_bool = ",bc_equals_zero_bool)

    if ac_equals_zero_bool and bc_equals_zero_bool:
        return_bool = True

    print(tab_amount,"return_bool = ",return_bool)
    return return_bool


if __name__ == "__main__":
    tab_amount = "\t"

    matrix_a = \
        [
            [1, 2, 3]
        ]
    matrix_b = \
        [
            [1, -1, 2]
        ]
    matrix_c = \
        [
            [7, 1, -3]
        ]

    print(get_if_three_matrices_are_perpendicular(matrix_a=matrix_a,matrix_b=matrix_b,matrix_c=matrix_c,tab_amount=tab_amount))
