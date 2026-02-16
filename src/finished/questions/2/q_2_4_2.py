from src.finished.print_matrix import print_matrix
from src.finished.operation_functions import *

def q_2_4_2(tab_amount="\t"):
    print(tab_amount,"q_2_4_2")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1,-3,-1,1],
        [2,-6,-2,2]
    ]
    scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/2,tab_amount=tab_amount+"\t")
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_2_4_2(tab_amount="")