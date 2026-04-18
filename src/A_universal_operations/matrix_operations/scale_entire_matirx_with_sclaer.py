from src.A_universal_operations.matrix_operations.matrix_operation_functions import *

def scale_entire_matrix_with_scaler(matrix, scaler, tab_amount="\t"):
    print(tab_amount,"scale_entire_matrix_with_scaler")
    tab_amount += "\t"
    for i in range(len(matrix)):
        scale_row_from_number(matrix=matrix,row_in_question=i,number=scaler,tab_amount=tab_amount)

    #the way python pointers work is wack as fuck.
    #this should be ok though :-/
    return matrix
