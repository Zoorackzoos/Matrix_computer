from src.A_universal_operations.matrix_operations.set_matrix_pivots_into_ones import *


def q_6_1_7_false(tab_amount="\t"):
    print(tab_amount,"q_6_1_7")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [9, -5, 19],
        [-1, 5, -11],
        [-5, 5, -15]
    ]
    get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    set_matrix_pivots_into_ones(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=5/9,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question, tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=9/5,tab_amount=tab_amount)
    print_matrix_frac(matrix_in_question=matrix_in_question, tab_amount=tab_amount)


if __name__ == "__main__":
    print("program started.")
    tab_amount = "\t"
    q_6_1_7_false(tab_amount=tab_amount)
    print("program ended.")