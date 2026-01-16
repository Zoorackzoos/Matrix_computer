from operation_functions import scale_row_from_row_and_number
from src.print_matrix import print_matrix
from src.tests import *


def q_1_1_5(tab_amount="\t"):
    print(tab_amount,"q_1_1_5")
    tab_amount += "\t"
    question_matrix = \
        [
            [1, -3, 2, "|", -4],
            [4, -11, -3, "|", 1],
            [-4, 8, -3, "|", -6]
        ]
    # r2 <- r2 + -4r1
    scale_row_from_row_and_number(question_matrix,1, 0, -4, tab_amount)
    print_matrix(question_matrix)
    scale_row_from_row_and_number(question_matrix,2, 0, 4, tab_amount)
    print_matrix(question_matrix)
    scale_row_from_row_and_number(question_matrix,2, 1, 4, tab_amount)
    print_matrix(question_matrix,tab_amount)

if __name__ == '__main__':
    matrix_in_question = \
        [
            [1, -3, 2, "|", -4],
            [4, -11, -3, "|", 1],
            [-4, 8, -3, "|", -6]
        ]

    print("program started")
    print("original matrix: ")
    print_matrix(matrix_in_question,"\t")
    test_scale_row_from_row_and_number(matrix_in_question)
