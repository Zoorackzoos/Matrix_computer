from src.A_universal_operations.calc_3_like_funcitons.convert_to_divided_by_sqrt import convert_to_divided_by_sqrt
from src.A_universal_operations.calc_3_like_funcitons.get_dot_product import get_dot_product
from src.A_universal_operations.calc_3_like_funcitons.get_magnitude import get_magnitude_of_matrix
from src.A_universal_operations.calc_3_like_funcitons.get_projection_with_2_matrixes import \
    get_projection_with_2_matrices
from src.A_universal_operations.display.print_matrix import print_matrix_frac
from src.A_universal_operations.matrix_operations.get_subtraction_result_of_two_matrixes import \
    get_subtraction_result_of_two_matrices


def q_7_1_6():
    tab_amount = "\t"

    p = \
    [
        [3,-2,1]
    ]
    A = \
    [
        [-4,0,4]
    ]
    B = \
    [
        [-1,-1,1]
    ]

    AP = get_subtraction_result_of_two_matrices(matrix_a=A,matrix_b=p,tab_amount=tab_amount)
    AB = get_subtraction_result_of_two_matrices(matrix_a=A,matrix_b=B,tab_amount=tab_amount)
    projection = get_projection_with_2_matrices(minority_matrix=AP,majority_matrix=AB,tab_amount=tab_amount)
    subtraciton_of_AP_and_projeciton = get_subtraction_result_of_two_matrices(matrix_a=projection,matrix_b=AP,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=subtraciton_of_AP_and_projeciton)
    magnitude = get_magnitude_of_matrix(matrix=subtraciton_of_AP_and_projeciton, tab_amount=tab_amount)
    pretty_magnitude = convert_to_divided_by_sqrt(number=magnitude,tab_amount=tab_amount)
    return pretty_magnitude

if __name__ == "__main__":
    print( q_7_1_6() )