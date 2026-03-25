

def get_diagonal_values_from_matrix(matrix_in_question,tab_amount="\t"):
    print(tab_amount,"get_diagonal_values_from_matrix")
    tab_amount += "\t"

    diagonal_values_list = []
    for diagonal_index in range(len(matrix_in_question)):
        diagonal_values_list.append(matrix_in_question[diagonal_index][diagonal_index])
    return diagonal_values_list