from src.display.print_matrix import *
from src.matrix_operations.check_if_matrix_is_all_zeros import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.get_REF import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.set_matrix_pivots_into_ones import *
from src.matrix_operations.vector_multiplier import *
from src.display.print_list_with_REF_matrix_and_scaler_operations import *

def q_6_1_9(tab_amount = "\t"):
    matrix_in_question = \
    [
        [0,2,1,"|",5],
        [3,-1,0,"|",4],
        [2,0,-3,"|",1]
    ]
    print_matrix(matrix_in_question=matrix_in_question, tab_amount=tab_amount)

if __name__ == "__main__":
    print("program started")
    tab_amount = "\t"
    q_6_1_9(tab_amount=tab_amount)
    print("program ended")