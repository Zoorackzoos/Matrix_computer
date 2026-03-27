import copy

from src.display.print_matrix import print_matrix
from src.matrix_operations.REF_both_pos_or_neg_helper import REF_both_pos_or_neg_helper
from src.matrix_operations.operation_functions import *

def get_RREF_from_REF(matrix_in_REF_form, tab_amount="\t"):
    print(tab_amount,"get_RREF_from_REF")
    tab_amount += "\t"
    """
    print_matrix
        [8, -40, -24]
        [0, 960, 448]
        [0, 0, -2]
    """
    num_of_rows = len(matrix_in_REF_form)
    num_of_columns = len(matrix_in_REF_form[0])

    row_index_a = 0
    row_index_b = 1
    column_index = 1

    old_matrix_in_REF_form = copy.deepcopy(matrix_in_REF_form)

    print(tab_amount,"loop time :DDD")
    tab_amount += "\t"

    #TODO: implement loop :-/ . work from down to up


if __name__ == "__main__":
    print("program started.")
    tab_amount = "\t"

    matrix_in_question = \
    [
        [8, -40, -24],
        [0, 960, 448],
        [0, 0, -2]
    ]
    get_RREF_from_REF(matrix_in_REF_form=matrix_in_question,tab_amount=tab_amount)
    print("program ended.")