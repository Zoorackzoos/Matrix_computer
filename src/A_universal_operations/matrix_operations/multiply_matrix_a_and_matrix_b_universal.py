from copy import deepcopy

def multiply_matrix_a_and_matrix_b_universal(matrix_a, matrix_b, tab_amount="\t"):
    """
    Credits to eat.shoe AKA Thomas, for finishing this function.
    it multiplies a 2 matrices of any size.

    :param tab_amount: this is just an amount of "\t"
    :param matrix_a: matrix of reasonable size
    :param matrix_b: matrix of reasonable size
    :return: the product of matrix_a and matrix_b
    """
    print(tab_amount, "multiply_matrix")
    tab_amount += "\t"

    # print_matrix(matrix=matrix_a, tab_amount=tab_amount)
    # print_matrix(matrix=matrix_b, tab_amount=tab_amount)

    matrixA_row_amount = len(matrix_a)
    matrixA_column_amount = len(matrix_a[0])

    matrixB_row_amount = len(matrix_b)
    matrixB_column_amount = len(matrix_b[0])
    # return_matrix = np.ones((matrixA_row_amount, matrixB_column_amount), dtype=int)

    if (matrixA_column_amount != matrixB_row_amount):
        exit("un-acceptable matrix multiplication n and m. exiting")

    print(tab_amount, "acceptable matrix multiplication n and m. continuing.")

    return_matrix_un_normalized = []

    for i in range(matrixA_row_amount):
        return_matrix_un_normalized.append([])
        for j in range(matrixB_column_amount):
            return_matrix_un_normalized[i].append(0)
            for k in range(matrixA_column_amount):
                return_matrix_un_normalized[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return return_matrix_un_normalized



"""
if __name__ == "__main__":
    print("program stated")
    matrix_a = \
        [
            [3, 2],
            [-3, -1],
            [-2, 0]
        ]
    matrix_b = \
        [
            [3, -2],
            [1, 3]
        ]
    result_matrix = multiply_matrix_universal(matrix_a=matrix_a, matrix_b=matrix_b, tab_amount="\t")
    print_matrix(result_matrix)
    print("program ended")
"""

