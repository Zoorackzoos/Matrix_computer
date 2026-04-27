from src.A_universal_operations.matrix_operations.get_if_three_matrices_are_perpandicular import \
    get_if_three_matrices_are_perpendicular
from src.A_universal_operations.display.print_matrix import print_matrix


def q_7_1_3_a(tab_amount = "\t"):
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

    return get_if_three_matrices_are_perpendicular(matrix_a=matrix_a, matrix_b=matrix_b, matrix_c=matrix_c,
                                                  tab_amount=tab_amount)

def q_7_1_3_b(tab_amount="\t"):
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
            [-7, -1, 3]
        ]

    return get_if_three_matrices_are_perpendicular(matrix_a=matrix_a, matrix_b=matrix_b, matrix_c=matrix_c,
                                                  tab_amount=tab_amount)

def q_7_1_3_c(tab_amount="\t"):
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
            [7, -1, -3]
        ]

    return get_if_three_matrices_are_perpendicular(matrix_a=matrix_a, matrix_b=matrix_b, matrix_c=matrix_c,
                                                  tab_amount=tab_amount)

def q_7_1_3_d(tab_amount="\t"):
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
            [1, -2, 6]
        ]

    return get_if_three_matrices_are_perpendicular(matrix_a=matrix_a, matrix_b=matrix_b, matrix_c=matrix_c,
                                                  tab_amount=tab_amount)

def q_7_1_3_e(tab_amount="\t"):
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
            [5, -5, 10]
        ]

    return get_if_three_matrices_are_perpendicular(matrix_a=matrix_a, matrix_b=matrix_b, matrix_c=matrix_c,
                                                  tab_amount=tab_amount)

if __name__ == "__main__":
    answers_list = \
        [
            q_7_1_3_a(),
            q_7_1_3_b(),
            q_7_1_3_c(),
            q_7_1_3_d(),
            q_7_1_3_e()
        ]

    print_matrix(matrix_in_question=answers_list)
