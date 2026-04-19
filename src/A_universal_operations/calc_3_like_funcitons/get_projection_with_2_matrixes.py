from src.A_universal_operations.calc_3_like_funcitons.get_dot_product import get_dot_product
from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string
from src.A_universal_operations.display.print_matrix import print_matrix, print_matrix_frac
from src.A_universal_operations.matrix_operations.scale_entire_matirx_with_sclaer import scale_entire_matrix_with_scaler


def get_projection_with_2_matrices(minority_matrix, majority_matrix, tab_amount="\t"):
    """
    proj_d * u
    =
    v * d ) * d
    /////
    d * d

    :param minority_matrix:
    :param majority_matrix:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_projection_with_2_matrices)")
    tab_amount += "\t"

    numerator = get_dot_product(matrix_a=minority_matrix, matrix_b=majority_matrix, tab_amount=tab_amount)
    print(tab_amount,"numerator -> ",numerator)

    denominator = get_dot_product(matrix_a=majority_matrix, matrix_b=majority_matrix, tab_amount=tab_amount)
    print(tab_amount,"denominator -> ",denominator)

    print()

    left_product = numerator / denominator
    print(tab_amount,"pure fraction to be functioned -> ",numerator," / ",denominator)
    left_product_fractionated = float_to_fraction_string(value=left_product, max_denominator=1000)
    print(tab_amount, "left_product_fractionated ->", left_product_fractionated)
    print(tab_amount,"left_product -> ",left_product)
    print(tab_amount,"matrix_b -> ")
    print_matrix(matrix_in_question=majority_matrix, tab_amount=tab_amount + "\t")

    print()

    final_product = scale_entire_matrix_with_scaler(matrix=majority_matrix, scaler=left_product, tab_amount=tab_amount)
    print(tab_amount,"final_product -> ")
    print_matrix_frac(matrix_in_question=final_product,tab_amount=tab_amount)

    return final_product

if __name__ == "__main__":
    matrix_a = \
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    matrix_b = \
    [
        [10,11,12],
        [13,14,15],
        [16,17,18]
    ]

    tab_amount = "\t"

    #probably fine. idk :-/
    get_projection_with_2_matrices(minority_matrix=matrix_a, majority_matrix=matrix_b, tab_amount=tab_amount)