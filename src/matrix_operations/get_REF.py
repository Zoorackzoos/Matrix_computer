import copy
import numbers

from src.display.print_matrix import *
from src.matrix_operations.REF_both_pos_or_neg_helper import REF_both_pos_or_neg_helper
from src.matrix_operations.check_if_matrix_is_all_zeros import get_if_matrix_is_all_zeros
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.set_matrix_pivots_into_ones import set_matrix_pivots_into_ones
from src.matrix_operations.vector_multiplier import *

def get_REF(matrix_in_question,tab_amount="\t"):
    """
    TODO: change this and it's brother function so that pivot rows that contain 0 are swapped or som shit.

    :param matrix_in_question: just a matrix bruh
    :param tab_amount: variations of "\t"
    :return: a REF matrix. NOT A RREF MATRIX DAMMIT
    """
    print(tab_amount,"get_REF")
    tab_amount += "\t"

    if len(matrix_in_question) == 0:
        print(tab_amount,"empty list. wtf dude.")
        #exit(2)
        return matrix_in_question

    if get_if_matrix_is_all_zeros(matrix_in_question=matrix_in_question,tab_amount=tab_amount):
        print(tab_amount,"this list is all zeros. wtf dude.")
        #exit(2)
        return matrix_in_question

    num_of_rows = len(matrix_in_question)
    num_of_columns = len(matrix_in_question[0])
    """
    1 2 3 -> 4 8 12 -> 4 8 12 ->28  56  84-> 28 56 84-> 20 56  84-> 20 56 84
    4 5 6    -4 -5 -6  0 3 6    0   3   6    0  3  6    0  72  144  0  72 144
    7 8 9    7 8 9     7 8 9    -28 -32 -36  0  24 48   0 -72 -144  0  0  0
    """
    print(tab_amount,"num_of_rows = ",num_of_rows)
    print(tab_amount,"num_of_columns = ",num_of_columns)

    row_index_a = 0
    row_index_b = 0
    column_index_shared = 0

    print(tab_amount,"loop time :DDD")
    tab_amount += "\t"

    while row_index_a < num_of_rows:
        print(tab_amount,"row_index_a = ",row_index_a)
        print(tab_amount,"row_index_a < num_of_rows = ","row_index_a < num_of_rows")
        print(tab_amount,"row_index_a < num_of_rows = ",row_index_a," < ",num_of_rows)
        print(tab_amount,"row_index_a < num_of_rows = ",row_index_a < num_of_rows)
        print()
        print(tab_amount, "row_index_b = ", row_index_b)
        print(tab_amount, "row_index_b < num_of_rows = ", "row_index_b < num_of_rows")
        print(tab_amount, "row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
        print(tab_amount, "row_index_b < num_of_rows = ", row_index_b < num_of_rows)

        able_to_go = False
        while able_to_go == False:
            if column_index_shared < num_of_columns:
                if matrix_in_question[row_index_a][column_index_shared] != 0:
                    able_to_go = True
                else:
                    column_index_shared += 1
            else:
                return matrix_in_question

        while row_index_b < num_of_rows:

            print(tab_amount + "\t", "row_index_b = ", row_index_b)
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", "row_index_b < num_of_rows")
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", row_index_b < num_of_rows)

            # if we're comparing the same rule. do nothing
            if matrix_in_question[row_index_a] == matrix_in_question[row_index_b]:
                print(tab_amount+"\t\t","we're comparing the same row. So no operation here.")
                row_index_b += 1
            else:
                old_matrix_in_question = copy.deepcopy(matrix_in_question)

                #if the row below contains a zero on our column_index_shared
                if (old_matrix_in_question[row_index_a][column_index_shared] == 0
                or
                old_matrix_in_question[row_index_b][column_index_shared] == 0):
                    print(tab_amount+"\t\t",f"either old_matrix_in_question[{row_index_a}][{column_index_shared}] or old_matrix_in_question[{row_index_b}][{column_index_shared}] is a 0. so no multiplication occurs here.")
                    row_index_b += 1
                else:
                    #multiplying the rows
                    print(tab_amount+"\t\t","multiplying the rows so we can get a pivot when we find the sum of both of them easier.")
                    scale_row_from_number(matrix=matrix_in_question,row_in_question=row_index_a,number=old_matrix_in_question[row_index_b][column_index_shared],tab_amount=tab_amount+"\t\t\t")
                    scale_row_from_number(matrix=matrix_in_question,row_in_question=row_index_b,number=old_matrix_in_question[row_index_a][column_index_shared],tab_amount=tab_amount+"\t\t\t")

                    #dealing with both positive and both negative rows.
                    print(tab_amount+"\t\t",f"is row {row_index_a} and row {row_index_b} both positive or both negative?")
                    both_rows_positive = (matrix_in_question[row_index_a][column_index_shared] > 0
                                            and
                                            matrix_in_question[row_index_b][column_index_shared] > 0)
                    both_rows_negative = (matrix_in_question[row_index_a][column_index_shared] < 0
                                            and
                                            matrix_in_question[row_index_b][column_index_shared] < 0)

                    if both_rows_positive or both_rows_negative:
                        print(tab_amount+"\t\t\t",f"They were either both positive or negative. So i set row {row_index_b} * -1")
                        scale_row_from_number(matrix=matrix_in_question,row_in_question=row_index_b,number=-1,tab_amount=tab_amount+"\t\t\t")
                    else:
                        print(tab_amount+"\t\t\t","they were opposite signs so no operation needed.")

                    #finding the sum of the 2 rows
                    print(tab_amount+"\t\t","finding the sum of the 2 rows.")
                    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=row_index_b,row_to_be_added=row_index_a,number=1,tab_amount=tab_amount+"\t\t\t")

                    #compare and contrast matrices.
                    print(tab_amount+"\t\t","matrix_in_question")
                    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount + "\t\t\t")
                    print(tab_amount+"\t\t","old_matrix_in_question")
                    print_matrix(matrix_in_question=old_matrix_in_question, tab_amount=tab_amount + "\t\t\t")

                    row_index_b += 1
                    print(tab_amount+"\t\t","reiterating row_index_b loop")
                    print(tab_amount+"\t\t","row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
        print(tab_amount,"back to row_index_a loop")

        """
        if column_index_shared == 1:
            print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
            exit(999)
        """

        row_index_a += 1
        column_index_shared += 1
        row_index_b = row_index_a
    return matrix_in_question

def get_list_with_REF_and_return_determinant_values(matrix_in_question, tab_amount="\t"):
    """
    TODO: change this and it's brother function so that pivot rows that contain 0 are swapped or som shit.

    gets the reduced echelon form but in a different return value way

    1. return value is a list that contains
        a. REF matrix
        b. operations used to get that REF matrix as a string
            that is repersented by how they wouuld be calculated
            if you were getting the determinant
                like if had to scale a row by 2,
                and another row by 5.
                I would add to this list:
                    1. 1/2
                    2. 1/5
                because once you get the REF you would multiply
                the diagonals and the scalers as fractions
        c. operations used to get that REF matrix as a float

    :param matrix_in_question: a matrix of any reasonable size
    :param tab_amount: variations of "\t"
    :return: a list that contains the matrix given with REF without normalization. that means that all the pivots are not 1s.
    """
    print(tab_amount,"get_REF")
    tab_amount += "\t"

    determinant_operation_string_values_list = []
    determinant_operation_numeric_values_list = []
    return_list = [matrix_in_question,determinant_operation_string_values_list,determinant_operation_numeric_values_list]

    if len(matrix_in_question) == 0:
        print(tab_amount, "empty list. wtf dude.")
        return return_list

    if get_if_matrix_is_all_zeros(matrix_in_question=matrix_in_question, tab_amount=tab_amount):
        print(tab_amount, "this list is all zeros. wtf dude.")
        return return_list

    num_of_rows = len(matrix_in_question)
    num_of_columns = len(matrix_in_question[0])

    print(tab_amount, "num_of_rows = ", num_of_rows)
    print(tab_amount, "num_of_columns = ", num_of_columns)

    row_index_a = 0
    row_index_b = 0
    column_index_shared = 0

    print(tab_amount, "loop time :DDD")
    tab_amount += "\t"

    while row_index_a < num_of_rows:
        print(tab_amount, "row_index_a = ", row_index_a)
        print(tab_amount, "row_index_a < num_of_rows = ", "row_index_a < num_of_rows")
        print(tab_amount, "row_index_a < num_of_rows = ", row_index_a, " < ", num_of_rows)
        print(tab_amount, "row_index_a < num_of_rows = ", row_index_a < num_of_rows)
        print()
        print(tab_amount, "row_index_b = ", row_index_b)
        print(tab_amount, "row_index_b < num_of_rows = ", "row_index_b < num_of_rows")
        print(tab_amount, "row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
        print(tab_amount, "row_index_b < num_of_rows = ", row_index_b < num_of_rows)

        able_to_go = False
        while able_to_go == False:
            if column_index_shared < num_of_columns:
                if matrix_in_question[row_index_a][column_index_shared] != 0:
                    able_to_go = True
                else:
                    column_index_shared += 1
            else:
                return return_list

        while row_index_b < num_of_rows:
            print(tab_amount + "\t", "row_index_b = ", row_index_b)
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", "row_index_b < num_of_rows")
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
            print(tab_amount + "\t", "row_index_b < num_of_rows = ", row_index_b < num_of_rows)

            # if we're comparing the same rule. do nothing
            if matrix_in_question[row_index_a] == matrix_in_question[row_index_b]:
                print(tab_amount + "\t\t", "we're comparing the same row. So no operation here.")
                row_index_b += 1
            else:
                old_matrix_in_question = copy.deepcopy(matrix_in_question)

                # if the row below contains a zero on our column_index_shared
                if (old_matrix_in_question[row_index_a][column_index_shared] == 0
                        or
                        old_matrix_in_question[row_index_b][column_index_shared] == 0):
                    print(tab_amount + "\t\t",
                          f"either old_matrix_in_question[{row_index_a}][{column_index_shared}] or old_matrix_in_question[{row_index_b}][{column_index_shared}] is a 0. so no multiplication occurs here.")
                    row_index_b += 1
                else:
                    # multiplying the rows
                    print(tab_amount + "\t\t",
                          "multiplying the rows so we can get a pivot when we find the sum of both of them easier.")
                    scale_row_from_number(matrix=matrix_in_question, row_in_question=row_index_a,
                                          number=old_matrix_in_question[row_index_b][column_index_shared],
                                          tab_amount=tab_amount + "\t\t\t")
                    scale_row_from_number(matrix=matrix_in_question, row_in_question=row_index_b,
                                          number=old_matrix_in_question[row_index_a][column_index_shared],
                                          tab_amount=tab_amount + "\t\t\t")
                    determinant_operation_string_values_list.append(f"1/{old_matrix_in_question[row_index_b][column_index_shared]}")
                    determinant_operation_string_values_list.append(f"1/{old_matrix_in_question[row_index_a][column_index_shared]}")
                    determinant_operation_numeric_values_list.append(1/old_matrix_in_question[row_index_b][column_index_shared])
                    determinant_operation_numeric_values_list.append(1/old_matrix_in_question[row_index_a][column_index_shared])

                    REF_both_pos_or_neg_helper(matrix_in_question=matrix_in_question, row_index_a=row_index_a, row_index_b=row_index_b, column_index_shared=column_index_shared, tab_amount=tab_amount)

                    # finding the sum of the 2 rows
                    print(tab_amount + "\t\t", "finding the sum of the 2 rows.")
                    scale_row_from_row_and_number(matrix=matrix_in_question, row_modified=row_index_b,
                                                  row_to_be_added=row_index_a, number=1,
                                                  tab_amount=tab_amount + "\t\t\t")

                    # compare and contrast matrices.
                    print(tab_amount + "\t\t", "matrix_in_question")
                    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount + "\t\t\t")
                    print(tab_amount + "\t\t", "old_matrix_in_question")
                    print_matrix(matrix_in_question=old_matrix_in_question, tab_amount=tab_amount + "\t\t\t")

                    row_index_b += 1
                    print(tab_amount + "\t\t", "reiterating row_index_b loop")
                    print(tab_amount + "\t\t", "row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
        print(tab_amount, "back to row_index_a loop")

        """
        if column_index_shared == 1:
            print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
            exit(999)
        """

        row_index_a += 1
        column_index_shared += 1
        row_index_b = row_index_a
    return return_list

def in_file_test_get_REF():
    print("start of program")
    matrix_in_question = \
        [
            [-5, 1, 11, 3],
            [-4, -5, 3, 3],
            [2, 3, -1, 4],
            [-5, -1, 9, 4]
        ]
    tab_amount = "\t"
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    matrix_in_question = set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question, tab_amount=tab_amount)

    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    print("end of program")

def in_file_test_get_REF_and_return_determinant_values():
    print("start of program")
    matrix_in_question = \
        [
            [-5, 1, 11, 3],
            [-4, -5, 3, 3],
            [2, 3, -1, 4],
            [-5, -1, 9, 4]
        ]
    tab_amount = "\t"
    output_matrix_and_operation_values_List = get_list_with_REF_and_return_determinant_values(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    print_matrix(matrix_in_question=output_matrix_and_operation_values_List[0], tab_amount=tab_amount)
    print(output_matrix_and_operation_values_List[1])

    print("end of program")

def in_file_test_get_REF_when_some_values_are_zero():
    print("start of program")
    tab_amount = "\t"
    matrix_in_question = \
        [
            [0, 2, 1, "|", 5],
            [3, -1, 0, "|", 4],
            [2, 0, -3, "|", 1]
        ]
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    print("end of program")

if __name__ == "__main__":
    in_file_test_get_REF_and_return_determinant_values()
