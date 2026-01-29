
"""
Find a set of vectors {u,v} in R^4 that spans the solution set of the equations
W + -x + -2y + 4z = 0
3w + 2x + -y + 3z = 0
U = [_ _ _ _]
V = [_ _ _ _]

"""

from src.print_matrix import print_matrix
from src.operation_functions import *

def q_2_2_10(tab_amount="\t"):
    print(tab_amount,"q_2_2_10")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1, -1, -2, 4, "|", 0],
        [3, 2, -1, 3, "|", 0],
    ]
    print_matrix(matrix_in_question, tab_amount)
    matrix_in_question = scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=1,row_to_be_added=0,number=-3,tab_amount=tab_amount+"\t")
    print_matrix(matrix_in_question, tab_amount)
    matrix_in_question = scale_row_from_row_and_number(matrix=matrix_in_question,row_modified=0,row_to_be_added=1,number=1/5,tab_amount=tab_amount+"\t")
    print_matrix(matrix_in_question, tab_amount)
    matrix_in_question = scale_row_from_number(matrix=matrix_in_question,row_in_question=1,number=1/5,tab_amount=tab_amount+"\t")
    print_matrix(matrix_in_question, tab_amount)

if __name__ == "__main__":
    q_2_2_10(tab_amount="")











