def swap_rows(matrix, row_1, row_2, tab_amount="\t"):
    """
    :param tab_amount:
    :param matrix:
    :param row_1: this needs to be a integer of the row. not r1,r2,r3 but 1,2,3
    :param row_2: this needs to be a integer of the row. not r1,r2,r3 but 1,2,3
    :return: the new matrix. even though the matrix_in_question variable will be edited
    """
    print(tab_amount,"swap_rows")
    tab_amount += "\t"

    row_1_content = matrix[row_1]
    print(tab_amount,"row_1_content = ",row_1_content)
    row_2_content = matrix[row_2]
    print(tab_amount,"row_2_content = ",row_2_content)

    matrix[row_2] = row_1_content
    matrix[row_1] = row_2_content

    return matrix

def scale_row_from_number(matrix, row_in_question, number, tab_amount="\t"):
    """
    :param matrix:
    :param row_in_question: this ia integer representing the row
    :param number: this is a integer, or a decimal that serpent a fraction
    :param tab_amount:
    :return:
    """
    print(tab_amount,"scale_row_from_number")
    tab_amount += "\t"
    print(tab_amount,"row_in_question = ",row_in_question)
    print(tab_amount,"number = ",number)
    matrix[row_in_question][0] *= number
    matrix[row_in_question][1] *= number
    matrix[row_in_question][2] *= number
    matrix[row_in_question][4] *= number
    return matrix

def scale_row_from_row_and_number(matrix, row_modified, row_to_be_added, number, tab_amount="\t"):
    """

    :param matrix:
    :param row_modified: this is the row that will be modified
    :param row_to_be_added: this is the row that will contribute the modified row
    :param number: this is the row that will also contribute to the modified row.
    :param tab_amount:
    :return:
    """
    print(tab_amount,"scale_row_from_row_and_number")
    tab_amount += "\t"
    print(tab_amount,"r",(row_modified+1)," <- r",(row_modified+1)," + ",(number),"r",(row_to_be_added+1))
    matrix[row_modified][0] = matrix[row_modified][0] + (number * matrix[row_to_be_added][0])
    matrix[row_modified][1] = matrix[row_modified][1] + (number * matrix[row_to_be_added][1])
    matrix[row_modified][2] = matrix[row_modified][2] + (number * matrix[row_to_be_added][2])
    matrix[row_modified][4] = matrix[row_modified][4] + (number * matrix[row_to_be_added][4])
    return matrix