from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def q_5_1_1(tab_amount="\t"):
    matrix_in_question = \
    [
        [-9,-4],
        [-4,-3]
    ]
    find_determinant_two_by_two_matrix(matrix=matrix_in_question,tab_amount=tab_amount)

if __name__ == "__main__":
    q_5_1_1(tab_amount="")