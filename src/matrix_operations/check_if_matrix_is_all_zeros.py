from src.display.print_matrix import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.vector_multiplier import *

def get_if_matrix_is_all_zeros(matrix_in_question, tab_amount="\t"):
    print(tab_amount,"check_if_matrix_is_all_zeros")
    tab_amount += "\t"
    print_matrix(matrix=matrix_in_question,tab_amount=tab_amount)
    for row in matrix_in_question:
        for column in row:
            if column != 0:
                return False
    return True