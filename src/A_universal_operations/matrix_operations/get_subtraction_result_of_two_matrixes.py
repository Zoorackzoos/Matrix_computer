def get_subtraction_result_of_two_matrices(matrix_a, matrix_b, tab_amount="\t"):
    print(tab_amount,"get_subtraction_result_of_two_matrices")
    tab_amount += "\t"

    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print(tab_amount,"matrix_a and matrix_b are not the same length. wtf dude")
        exit(999)

    result_matrix = matrix_b

    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            result_matrix[row][col] -= matrix_a[row][col]

    return result_matrix