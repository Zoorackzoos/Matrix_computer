from src.A_universal_operations.display.print_matrix import *

def print_list_with_REF_matrix_and_scaler_operations(list_with_REF_matrix_and_scaler_operations, tab_amount="\t"):
    print(tab_amount,"print_list_with_REF_matrix_and_scaler_operations")
    tab_amount += "\t"
    print_matrix(matrix_in_question=list_with_REF_matrix_and_scaler_operations[0], tab_amount=tab_amount)
    print(tab_amount,list_with_REF_matrix_and_scaler_operations[1])