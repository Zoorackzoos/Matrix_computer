from src.finished.print_matrix import print_matrix, print_matrix_frac
from src.finished.operation_functions import *

def exam_1_q_7(tab_amount = ""):
    print(tab_amount,"exam_1_q_7")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1, 2, 3, 5, 1, 7, 4, 2, "|", 9],
        [2, 4, 1, 3, 5, 9, 6, 1, "|", 7],
        [1, 2, 0, 1, 1, 5, 2, 0, "|", 3],
        [0, 0, 2, 4, 1, 3, 5, 2, "|", 1],
        [1, 2, 1, 2, 3, 8, 3, 1, "|", 5],
        [2, 4, 2, 4, 4, 11, 7, 3, "|", 9],
    ]
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=2,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=2,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=-6,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=5,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=2,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=15,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=1,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=5,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=5,row_to_be_added=4,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=4,row_to_be_added=0,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=4,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=30,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=4,row_to_be_added=1,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=10,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=8,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=3,row_to_be_added=2,number=-1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=80,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=12,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=4,row_to_be_added=2,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=4800,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=1950,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=4,row_to_be_added=3,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=4680000,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=5,row_to_be_added=3,number=1,tab_amount=tab_amount)
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/1,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/120,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1/960,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=1/9360000,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=1/33840000,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=-1/27000000,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=5,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=2,number=1,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=3,number=13,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=47,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=75,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=75,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=47,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=5,row_to_be_added=4,number=-1,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=1/3525,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=-1/1157,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=4,number=47,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=5,number=89,tab_amount=tab_amount)
    print_matrix_frac(matrix=matrix_in_question)
    # whatever




if __name__ == "__main__":
    exam_1_q_7()











