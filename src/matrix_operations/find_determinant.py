def find_determinant_two_by_two_matrix(matrix, tab_amount="\t"):
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

def find_determinant_based_on_fed_array_values(list_of_fed_values,tab_amount="\t"):
    print(tab_amount,list_of_fed_values)
    tab_amount += "\t"
    total = 1
    for element in list_of_fed_values:
        total *= element
        print(tab_amount,"* ",element)
    tab_amount += "\t"
    print(tab_amount,total)

if __name__ == "__main__":
    print("hello me, meet the real me.")