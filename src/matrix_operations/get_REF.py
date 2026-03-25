import copy
import numbers

from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def get_if_matrix_is_all_zeros(matrix_in_question, tab_amount="\t"):
    print(tab_amount,"check_if_matrix_is_all_zeros")
    tab_amount += "\t"
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    for row in matrix_in_question:
        for column in row:
            if column != 0:
                return False
    return True

#TODO: finish implementing this dog ahh function
def get_REF(matrix_in_question,tab_amount="\t"):
    """
    gets row echelon form

    example operations done by this function:
        scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=4,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-1,tab_amount=tab_amount)
        scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=1,tab_amount=tab_amount)

        scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=7,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=4,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1,tab_amount=tab_amount)
        scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=1,tab_amount=tab_amount)

        scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=24,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=3,tab_amount=tab_amount)
        scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=-1,tab_amount=tab_amount)
        scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)

    :param matrix_in_question: just a matrix. doesn't matter the size
    :param tab_amount: various amounts of "\t". like "\t\t" or "\t\t\t"
    :return: nothing. somehow matrix in question changes when fed into functions despite not returning.
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
    column_index_a = 0
    column_index_b = 0
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
                print_matrix(matrix=matrix_in_question,tab_amount=tab_amount+"\t\t\t")
                print(tab_amount+"\t\t","old_matrix_in_question")
                print_matrix(matrix=old_matrix_in_question,tab_amount=tab_amount+"\t\t\t")

                row_index_b += 1
                print(tab_amount+"\t\t","reiterating row_index_b loop")
                print(tab_amount+"\t\t","row_index_b < num_of_rows = ", row_index_b, " < ", num_of_rows)
        print(tab_amount,"back to row_index_a loop")

        row_index_a += 1
        column_index_shared += 1
        row_index_b = row_index_a
    return matrix_in_question

if __name__ == "__main__":
    print("start of program")
    matrix_in_question = \
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    tab_amount = "\t"
    get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)

    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    print("end of program")