from src.A_universal_operations.display.print_list_with_REF_matrix_and_scaler_operations import *

def q_5_2_4_a(tab_amount="\t"):
    print(tab_amount,"q_5_2_4_a")
    tab_amount += "\t"

    matrix_a = \
    [
        [-5,1,11,3],
        [-4,-5,3,3],
        [2,3,-1,4],
        [-5,-1,9,4]
    ]
    matrix_a_REF_and_scaler_ops_list = get_list_with_REF_and_return_determinant_values(matrix_in_question=matrix_a,tab_amount=tab_amount)
    print_list_with_REF_matrix_and_scaler_operations(list_with_REF_matrix_and_scaler_operations=matrix_a_REF_and_scaler_ops_list,tab_amount=tab_amount)

    matrix_a_determinant = get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(list_with_REF_matrix_and_scaler_operations_in_it=matrix_a_REF_and_scaler_ops_list,tab_amount=tab_amount)
    print(tab_amount,"matrix_a_determinant = ",matrix_a_determinant)

def q_5_2_4_b(tab_amount="\t"):
    print(tab_amount,"q_5_2_4_b")
    tab_amount += "\t"

    matrix_b = \
    [
        [-3,9,18,36],
        [5,-13,-24,-45],
        [-1,1,-2,-7],
        [-1,3,6,12]
    ]
    matrix_b_REF_and_scaler_ops_list = get_list_with_REF_and_return_determinant_values(matrix_in_question=matrix_b,tab_amount=tab_amount)
    print_list_with_REF_matrix_and_scaler_operations(list_with_REF_matrix_and_scaler_operations=matrix_b_REF_and_scaler_ops_list,tab_amount=tab_amount)

    determinant_of_matrix_b = get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(list_with_REF_matrix_and_scaler_operations_in_it=matrix_b_REF_and_scaler_ops_list,tab_amount=tab_amount)
    print(tab_amount,"determinant_of_matrix_b = ",determinant_of_matrix_b)

def q_5_2_4_c(tab_amount="\t"):
    print(tab_amount,"q_5_2_4_c")
    tab_amount += "\t"

    matrix_c = \
        [
            [4, 3, -6],
            [-1, 1, 5],
            [-1, 1, 5]
        ]
    #uhh ok...
    matrix_c_REF_and_scaler_ops_list = get_list_with_REF_and_return_determinant_values(matrix_in_question=matrix_c,tab_amount=tab_amount)
    print_list_with_REF_matrix_and_scaler_operations(list_with_REF_matrix_and_scaler_operations=matrix_c_REF_and_scaler_ops_list,tab_amount=tab_amount)

    determinant_of_matrix_c = get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(
        list_with_REF_matrix_and_scaler_operations_in_it=matrix_c_REF_and_scaler_ops_list, tab_amount=tab_amount)
    print(tab_amount, "determinant_of_matrix_c = ", determinant_of_matrix_c)

def q_5_2_4_d(tab_amount="\t"):
    print(tab_amount,"q_5_2_4_d")
    tab_amount += "\t"

    matrix_d = \
    [
        [-4, -16, -4],
        [-2, -9, -3],
        [4, 17, 2]
    ]

    matrix_d_REF_and_scaler_ops_list = get_list_with_REF_and_return_determinant_values(matrix_in_question=matrix_d,
                                                                                       tab_amount=tab_amount)
    print_list_with_REF_matrix_and_scaler_operations(
        list_with_REF_matrix_and_scaler_operations=matrix_d_REF_and_scaler_ops_list, tab_amount=tab_amount)

    determinant_of_matrix_d = get_determinant_based_on_list_with_REF_matrix_and_scaler_operations_in_it(
        list_with_REF_matrix_and_scaler_operations_in_it=matrix_d_REF_and_scaler_ops_list, tab_amount=tab_amount)
    print(tab_amount, "determinant_of_matrix_d = ", determinant_of_matrix_d)

if __name__ == "__main__":
    print("program started")
    tab_amount = "\t"

    #q_5_2_4_a(tab_amount=tab_amount)
    #q_5_2_4_b(tab_amount=tab_amount)
    #q_5_2_4_c(tab_amount=tab_amount)
    q_5_2_4_d(tab_amount=tab_amount)

    print("program ended")