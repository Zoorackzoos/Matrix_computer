from src.display.print_matrix import *
from src.matrix_operations.check_if_matrix_is_all_zeros import *
from src.matrix_operations.find_determinant import *
from src.matrix_operations.get_REF import *
from src.matrix_operations.operation_functions import *
from src.matrix_operations.set_matrix_pivots_into_ones import *
from src.matrix_operations.vector_multiplier import *
from src.display.print_list_with_REF_matrix_and_scaler_operations import *

def week_10_chapter_5_worksheet_q_3(tab_amount="\t"):
    print(tab_amount,"week_10_chapter_5_worksheet_q_3")
    tab_amount += "\t"
    matrix_in_question = \
    [
        [1,-5,-3],
        [2,5,1],
        [4,12,3]
    ]
    matrix_in_question = get_REF(matrix_in_question=matrix_in_question,tab_amount=tab_amount)
    print_matrix(matrix_in_question)
    #TODO: add conditional in get_REF and sister function to have a conditional for 1s in either row

if __name__ == "__main__":
    tab_amount = "\t"
    week_10_chapter_5_worksheet_q_3(tab_amount=tab_amount)