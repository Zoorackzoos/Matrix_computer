"""
these functions do matrix operations.
* swap rows
* scale a row by a number (scaler)
* scale a row by a number multiplied by another row
"""

def swap_rows(matrix_in_question, row_1, row_2, tab_amount="\t"):
    """
    swaps rows in a matrix.

    :param tab_amount: variations of "\t"
    :param matrix_in_question: matrix of a any size
    :param row_1: this needs to be a integer of the row. not r1,r2,r3 but 0,1,2
    :param row_2: this needs to be a integer of the row. not r1,r2,r3 but 0,1,2
    :return: the new matrix. matrix_in_question will be edited anyway somehow, but if someone is anal they can have this too.
    """
    print(tab_amount,"swap_rows")
    tab_amount += "\t"

    row_1_content = matrix_in_question[row_1]
    print(tab_amount,"row_1_content = ",row_1_content)
    row_2_content = matrix_in_question[row_2]
    print(tab_amount,"row_2_content = ",row_2_content)

    matrix_in_question[row_2] = row_1_content
    matrix_in_question[row_1] = row_2_content

    return matrix_in_question

def scale_row_from_number(matrix, row_in_question, number, tab_amount="\t"):
    """
    :param matrix: matrix of reasonable size
    :param row_in_question: this ia integer representing the row
    :param number: this is a integer, or a decimal that serpent a fraction
    :param tab_amount: variations of "\t
    :return: the result of the edited matrix. matrix_in_question will be edited anyway but if you're anal this is for you.
    """
    print(tab_amount,"scale_row_from_number")
    tab_amount += "\t"
    print(tab_amount,"row_in_question = ",row_in_question)
    print(tab_amount,"number = ",number)
    for i in range(len(matrix[row_in_question])):
        #print(tab_amount+"\t","i = ",i)
        #print(tab_amount+"\t","matrix[row_in_question][i] = ",matrix[row_in_question][i])
        if matrix[row_in_question][i] != "|":
            matrix[row_in_question][i] *= number
        else:
            print(tab_amount+"\t\t","i see | so this is a augmented matrix.")

    return matrix

def scale_row_from_row_and_number(matrix, row_modified, row_to_be_added, number, tab_amount="\t"):
    """
    :param matrix: matrix of reasonable size
    :param row_modified: this is the row that will be modified
    :param row_to_be_added: this is the row that will contribute the modified row
    :param number: this is the row that will also contribute to the modified row.
    :param tab_amount: variations of "\t"
    :return: the edited matrix. matrix_in_question will be edited anyway.
    """
    print(tab_amount,"scale_row_from_row_and_number")
    tab_amount += "\t"
    print(tab_amount,"r",(row_modified+1)," <- r",(row_modified+1)," + ",(number),"r",(row_to_be_added+1))
    for i in range(len(matrix[row_modified])):
        print(tab_amount+"\t", ( matrix[row_modified][i] ), " <- ", matrix[row_modified][i], " + ", (number), " * ", matrix[row_to_be_added][i])
        if matrix[row_modified][i] != "|":
            print(tab_amount + "\t\t", (matrix[row_modified][i] + (number * matrix[row_to_be_added][i])), " <- ",matrix[row_modified][i], " + ", (number) * matrix[row_to_be_added][i])
            matrix[row_modified][i] = matrix[row_modified][i] + (number * matrix[row_to_be_added][i])
        else:
            print(tab_amount+"\t\t","i see | so this is a augmented matrix.")
    return matrix