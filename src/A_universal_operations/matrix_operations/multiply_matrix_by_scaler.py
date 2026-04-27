from copy import deepcopy


def multiply_matrix_by_scaler(matrix_a, scaler, tab_amount="\t"):
    print(tab_amount, "multiply_matrix_by_scaler")
    tab_amount += "\t"

    result_matrix = deepcopy(matrix_a)

    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            result_matrix[i][j] = result_matrix[i][j] * scaler

    return result_matrix