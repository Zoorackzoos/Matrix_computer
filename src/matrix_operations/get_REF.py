import copy
import numbers

from src.display.print_matrix import *
from src.matrix_operations.check_if_matrix_is_all_zeros import get_if_matrix_is_all_zeros
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.set_matrix_pivots_into_ones import set_matrix_pivots_into_ones
from src.matrix_operations.vector_multiplier import *

def get_REF(matrix_in_question,tab_amount="\t"):
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

        """
        if column_index_shared == 1:
            print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
            exit(999)
        """

        row_index_a += 1
        column_index_shared += 1
        row_index_b = row_index_a
    return matrix_in_question

def GPT_get_REF(matrix_in_question, tab_amount="\t"):
    """
    kind've a piece of junk

    :param matrix_in_question:
    :param tab_amount:
    :return:
    """
    print(tab_amount, "get_REF")
    tab_amount += "\t"

    if len(matrix_in_question) == 0:
        return matrix_in_question

    num_rows = len(matrix_in_question)
    num_cols = len(matrix_in_question[0])

    pivot_row = 0

    for col in range(num_cols):
        if pivot_row >= num_rows:
            break

        # 🔹 Find pivot
        pivot = None
        for r in range(pivot_row, num_rows):
            if matrix_in_question[r][col] != 0:
                pivot = r
                break

        if pivot is None:
            continue

        # 🔹 Swap rows if needed
        if pivot != pivot_row:
            matrix_in_question[pivot_row], matrix_in_question[pivot] = \
                matrix_in_question[pivot], matrix_in_question[pivot_row]


        # 🔹 Eliminate below
        for r in range(pivot_row + 1, num_rows):
            if matrix_in_question[r][col] != 0:
                factor = matrix_in_question[r][col] / matrix_in_question[pivot_row][col]

                for c in range(col, num_cols):
                    matrix_in_question[r][c] -= factor * matrix_in_question[pivot_row][c]

        pivot_row += 1


    return matrix_in_question



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
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    matrix_in_question = set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question,tab_amount=tab_amount)

    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    print("end of program")