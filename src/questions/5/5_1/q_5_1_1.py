from src.matrix_operations.determinant_getters.find_determinant import *


def q_5_1_1(tab_amount="\t"):
    matrix_in_question = \
    [
        [-9,-4],
        [-4,-3]
    ]
    get_determinant_two_by_two_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)

if __name__ == "__main__":
    q_5_1_1(tab_amount="")