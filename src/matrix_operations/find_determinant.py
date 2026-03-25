from src.matrix_operations.get_REF import *

def get_determinant_two_by_two_matrix(matrix, tab_amount="\t"):
    """

    :param matrix: a 2 x 2 matrix
    :return: the determinant as dictated by a*d - b*c
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    return_value = a*d - b*c
    print(tab_amount,return_value)
    return return_value

def get_determinant_based_on_list_of_fed_values(list_of_fed_values, tab_amount="\t"):
    print(tab_amount,list_of_fed_values)
    tab_amount += "\t"
    total = 1
    for element in list_of_fed_values:
        total *= element
        print(tab_amount,"* ",element)
    tab_amount += "\t"
    print(tab_amount,total)

def get_diagonal_values_from_matrix(matrix_in_question,tab_amount="\t"):
    print(tab_amount,"get_diagonal_values_from_matrix")
    tab_amount += "\t"

    diagonal_values_list = []
    for diagonal_index in range(len(matrix_in_question)):
        diagonal_values_list.append(matrix_in_question[diagonal_index][diagonal_index])
    return diagonal_values_list

def get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(list_with_REF_matrix_and_scaler_operations_in_it,tab_amount="\t"):
    print(tab_amount,"get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it")
    tab_amount += "\t"

    #making product of diagonal values list
    diagonal_values_list = get_diagonal_values_from_matrix(matrix_in_question=list_with_REF_matrix_and_scaler_operations_in_it[0],tab_amount=tab_amount)

    product_of_diagonal_values_list = diagonal_values_list[0]
    diagonal_values_list_index = 1

    while diagonal_values_list_index < len(diagonal_values_list):
        product_of_diagonal_values_list *= diagonal_values_list[diagonal_values_list_index]
        diagonal_values_list_index += 1

    return product_of_diagonal_values_list

if __name__ == "__main__":
    print("start of program")
    matrix_in_question = \
        [
            [-5, 1, 11, 3],
            [-4, -5, 3, 3],
            [2, 3, -1, 4],
            [-5, -1, 9, 4]
        ]

    tab_amount = "\t"

    REF_of_matrix_in_question_and_its_determinant_values = get_REF_and_return_determinant_values(matrix_in_question=matrix_in_question,tab_amount=tab_amount)

    print_matrix(REF_of_matrix_in_question_and_its_determinant_values[0],tab_amount=tab_amount)
    print(tab_amount,REF_of_matrix_in_question_and_its_determinant_values[1])

    determinant = get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(list_with_REF_matrix_and_scaler_operations_in_it=REF_of_matrix_in_question_and_its_determinant_values,tab_amount=tab_amount)
    print(tab_amount,determinant)
    print("end of program")