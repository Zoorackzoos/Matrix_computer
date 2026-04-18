from src.A_universal_operations.display.print_matrix import print_matrix

def get_if_matrix_is_all_zeros(matrix_in_question, tab_amount="\t"):
    """
    if the matrix contains only 0 elements this returns true.
    if otherwise it returns false.

    :param matrix_in_question: regular matrix of any size.
    :param tab_amount: variations of "\t".
    :return: bool value, either true or false.
    """
    print(tab_amount,"check_if_matrix_is_all_zeros")
    tab_amount += "\t"
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    for row in matrix_in_question:
        for column in row:
            if column != 0:
                return False
    return True