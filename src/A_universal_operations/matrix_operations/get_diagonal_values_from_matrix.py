

def get_diagonal_values_from_matrix(matrix_in_question,tab_amount="\t"):
    """
    this returns a list variable containing all the diagonal values in a matrix.
    this is mostly useful if you're getting determinant from a matrx in REF.

    :param matrix_in_question: a matrix of reasonable size
    :param tab_amount: variations of "\t"
    :return: list variable containing all diagonal values.
    """
    print(tab_amount,"get_diagonal_values_from_matrix")
    tab_amount += "\t"

    diagonal_values_list = []
    for diagonal_index in range(len(matrix_in_question)):
        diagonal_values_list.append(matrix_in_question[diagonal_index][diagonal_index])
    return diagonal_values_list