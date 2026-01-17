from src.operation_functions import scale_row_from_number, scale_row_from_row_and_number
from src.print_matrix import print_matrix


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

def q_1_1_7(tab_amount="\t"):
    print(tab_amount,"q_1_1_7")
    tab_amount += "\t"
    matrix_a = \
    [
        [2, 4, -6, "|", 12],
        [-3, -6, 9, "|", 16]
    ]
    matrix_b = \
    [
        [2, 4, -6, "|", 12],
        [-1, 5, -9, "|", 1]
    ]
    matrix_c = \
    [
        [2, 4, -6, "|", -12],
        [-3, -6, 9, "|", 18]
    ]
    #matrix_a
    q_1_1_7_process_matrix_a(matrix_a, tab_amount)
    #matrix_b
    q_1_1_7_process_matrix_b(matrix_b, tab_amount)
    #matrix_c
    q_1_1_7_process_matrix_c(matrix_c, tab_amount)


def q_1_1_7_process_matrix_c(matrix_c: list[list[int | str]], tab_amount: str):
    print(tab_amount, "matrix_c")
    print_matrix(matrix_c, tab_amount + "\t")
    scale_row_from_number(matrix_c, 0, 3, tab_amount + "\t")
    scale_row_from_number(matrix_c, 1, -2, tab_amount + "\t")
    print_matrix(matrix_c, tab_amount + "\t")
    print(tab_amount + "\t", "oh they're just teh same thing lol.")


def q_1_1_7_process_matrix_b(matrix_b: list[list[int | str]], tab_amount: str):
    print(tab_amount, "matrix_b")
    print_matrix(matrix_b, tab_amount + "\t")
    scale_row_from_number(matrix=matrix_b, row_in_question=1, number=-2, tab_amount=tab_amount + "\t")
    print_matrix(matrix_b, tab_amount + "\t")
    scale_row_from_number(matrix=matrix_b, row_in_question=0, number=1 / 2, tab_amount=tab_amount + "\t")
    scale_row_from_number(matrix=matrix_b, row_in_question=1, number=1 / 2, tab_amount=tab_amount + "\t")
    print_matrix(matrix_b, tab_amount + "\t")
    scale_row_from_row_and_number(matrix=matrix_b, row_modified=1, row_to_be_added=0, number=-1,
                                  tab_amount=tab_amount + "\t")
    print_matrix(matrix_b, tab_amount + "\t")
    scale_row_from_number(matrix=matrix_b, row_in_question=1, number=-1 / 7, tab_amount=tab_amount + "\t")
    print_matrix(matrix_b, tab_amount + "\t")
    print(tab_amount + "\t", "this is probably two lines intersecting a point :-/ ")


def q_1_1_7_process_matrix_a(matrix_a: list[list[int | str]], tab_amount: str):
    print(tab_amount, "matrix_a")
    print_matrix(matrix_a, tab_amount + "\t")
    scale_row_from_number(matrix=matrix_a, row_in_question=0, number=(-3 / 2), tab_amount=tab_amount + "\t")
    print_matrix(matrix_a, tab_amount + "\t")
    print(tab_amount + "\t",
          "this is a indicator of 2 parallel planes. i don't think i'll add a detector for that quite yet.")