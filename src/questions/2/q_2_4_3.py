from src.print_matrix import print_matrix, print_matrix_frac
from src.operation_functions import *

def q_2_4_3(tab_amount="\t"):
    print(tab_amount,"q_2_4_3")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1,4,4,-3,'|',1],
        [2,8,8,-6,'|',2]
    ]
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=2,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    scale_row_from_number(matrix=matrix_in_question,row_in_question=0,number=1/2,tab_amount=tab_amount+"\t")
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_2_4_3(tab_amount="")