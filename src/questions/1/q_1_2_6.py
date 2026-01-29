from src.print_matrix import *
from src.operation_functions import *

def q_1_2_6(tab_amount="\t"):
    print(tab_amount,"q_1_2_6")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [-2, -4, -8, "|", 8],
        [2, -4, -1, "|", -3],
        [10, -12, "h", "|", "k"]
    ]
    print_matrix(matrix=matrix_in_question)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=5,tab_amount=tab_amount+"\t")
    print_matrix_frac(matrix=matrix_in_question)