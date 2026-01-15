from tokenize import String

matrix_in_question = \
[
    [1, -3, 2, "|", -4],
    [4, -11, -3, "|", 1],
    [-4, 8, -3, "|", -6]
]

def print_matrix(matrix, tab_amount="\t"):
    print(tab_amount,"print_matrix")
    for row in matrix:
        print(tab_amount+"\t",row)

def swap_rows(row_1, row_2, tab_amount="\t"):
    """
    :param row_1: this needs to be a integer of the row. not r1,r2,r3 but 1,2,3
    :param row_2: this needs to be a integer of the row. not r1,r2,r3 but 1,2,3
    :return: the new matrix. even though the matrix_in_question variable will be edited
    """
    print(tab_amount,"swap_rows")
    tab_amount += "\t"
    old_matrix = matrix_in_question

    row_1_content = matrix_in_question[row_1]
    print(tab_amount,"row_1_content = ",row_1_content)
    row_2_content = matrix_in_question[row_2]
    print(tab_amount,"row_2_content = ",row_2_content)

    matrix_in_question[row_2] = row_1_content
    matrix_in_question[row_1] = row_2_content

    return matrix_in_question

def scale_row_from_number(row_in_question, number, tab_amount="\t"):
    """
    :param row_in_question: this ia integer representing the row
    :param number: this is a integer, or a decimal that serpent a fraction
    :param tab_amount:
    :return:
    """
    print(tab_amount,"scale_row_from_number")
    tab_amount += "\t"
    print(tab_amount,"row_in_question = ",row_in_question)
    print(tab_amount,"number = ",number)
    matrix_in_question[row_in_question][0] *= number
    matrix_in_question[row_in_question][1] *= number
    matrix_in_question[row_in_question][2] *= number
    matrix_in_question[row_in_question][4] *= number
    return matrix_in_question

def scale_row_from_row_and_number(row_modified, row_to_be_added, number, tab_amount="\t"):
    """

    :param row_modified: this is the row that will be modified
    :param row_to_be_added: this is the row that will contribute the modified row
    :param number: this is the row that will also contribute to the modified row.
    :param tab_amount:
    :return:
    """
    print(tab_amount,"scale_row_from_row_and_number")
    tab_amount += "\t"
    print(tab_amount,"r",(row_modified+1)," <- r",(row_modified+1)," + ",(number),"r",(row_to_be_added+1))
    matrix_in_question[row_modified][0] = matrix_in_question[row_modified][0] + (number * matrix_in_question[row_to_be_added][0])
    matrix_in_question[row_modified][1] = matrix_in_question[row_modified][1] + (number * matrix_in_question[row_to_be_added][1])
    matrix_in_question[row_modified][2] = matrix_in_question[row_modified][2] + (number * matrix_in_question[row_to_be_added][2])
    matrix_in_question[row_modified][4] = matrix_in_question[row_modified][4] + (number * matrix_in_question[row_to_be_added][4])
    return matrix_in_question

if __name__ == '__main__':
    print("program started")
    print("original matrix: ")
    print_matrix(matrix_in_question,"\t")
    """
    #swapping rows test.
    swap_rows(0,1)
    print("swapped row 1 and 2 in the matrix: ")
    print_matrix(matrix_in_question,"\t")
    """
    """
    #scale row from number test
    scale_row_from_number(0,2,"\t")
    print_matrix(matrix_in_question)
    """
    """
    #scale_row_from_row_and_number test
    # r2 <- r2 + -4r1
    scale_row_from_row_and_number(1,0,-4, "\t")
    print_matrix(matrix_in_question)
    """
    # r2 <- r2 + -4r1
    scale_row_from_row_and_number(1, 0, -4, "\t")
    print_matrix(matrix_in_question)
    scale_row_from_row_and_number(2, 0, 4, "\t")
    print_matrix(matrix_in_question)
    scale_row_from_row_and_number(2, 1, 4, "\t")
    print_matrix(matrix_in_question)