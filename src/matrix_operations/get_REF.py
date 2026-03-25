import copy
import numbers

from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def get_if_matrix_is_all_zeros(matrix_in_question, tab_amount="\t"):
    print(tab_amount,"check_if_matrix_is_all_zeros")
    tab_amount += "\t"
    for row in matrix_in_question:
        for column in row:
            if isinstance(matrix_in_question[row][column], numbers.Number):
                return True
    return False

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
        print("empty list. wtf dude.")
        exit(2)

    if get_if_matrix_is_all_zeros(matrix_in_question=matrix_in_question,tab_amount=tab_amount):
        print("this list is all zeros. wtf dude.")
        exit(2)

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

    while row_index_a < num_of_rows:
        while row_index_b < num_of_columns:


    exit(999)

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