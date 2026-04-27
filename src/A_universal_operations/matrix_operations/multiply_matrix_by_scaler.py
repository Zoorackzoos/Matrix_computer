from copy import deepcopy

from src.A_universal_operations.matrix_operations.matrix_operation_functions import *

def multiply_matrix_by_scaler(matrix, scaler, tab_amount="\t"):
    print(tab_amount,"multiply_matrix_by_scaler")
    tab_amount += "\t"

    temp_matrix = deepcopy(matrix)

    for i in range(len(temp_matrix)):
        scale_row_from_number(matrix=temp_matrix,row_in_question=i,number=scaler,tab_amount=tab_amount)

    #the way python pointers work is wack as fuck.
    #this should be ok though :-/
    return temp_matrix
