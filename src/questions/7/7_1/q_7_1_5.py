from src.A_universal_operations.calc_3_like_funcitons.get_magnitude import get_magnitude_of_matrix
from src.A_universal_operations.calc_3_like_funcitons.get_projection_with_2_matrixes import \
    get_projection_with_2_matrices
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import \
    get_subtraction_result_of_two_matrices


def q_7_1_5():
    y = \
    [
        [2],
        [3]
    ]
    u = \
    [
        [2],
        [4]
    ]
    tab_amount = "\t"
    projection = get_projection_with_2_matrices(minority_matrix=y,majority_matrix=u,tab_amount=tab_amount)

    subtracted_projection = get_subtraction_result_of_two_matrices(matrix_a=y,matrix_b=u,tab_amount=tab_amount)
    get_magnitude_of_matrix(matrix=subtracted_projection, tab_amount="\t")

if __name__ == "__main__":
    q_7_1_5()