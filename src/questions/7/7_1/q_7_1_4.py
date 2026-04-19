from src.A_universal_operations.calc_3_like_funcitons.get_projection_with_2_matrixes import \
    get_projection_with_2_matrices


def q_7_1_4():
    v = \
    [
        [4],
        [-5]
    ]
    L = \
    [
        [7],
        [2]
    ]
    tab_amount="\t"
    get_projection_with_2_matrices(minority_matrix=v,majority_matrix=L,tab_amount=tab_amount)

if __name__ == "__main__":
    q_7_1_4()