from copy import deepcopy

from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string


def matrix_float_to_fraction_string(matrix, tab_amount="\t"):
    print(tab_amount,"matrix_float_to_fraction_string")
    tab_amount += "\t"
    result_matrix = deepcopy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = float_to_fraction_string(matrix[i][j])

    return result_matrix