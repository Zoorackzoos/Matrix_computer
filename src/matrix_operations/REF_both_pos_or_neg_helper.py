from src.matrix_operations.operation_functions import scale_row_from_number


def REF_both_pos_or_neg_helper(matrix_in_question, row_index_a, row_index_b, column_index_shared, tab_amount="\t"):
    """
     # dealing with both positive and both negative rows.
    print(tab_amount + "\t\t",
          f"is row {row_index_a} and row {row_index_b} both positive or both negative?")
    both_rows_positive = (matrix_in_question[row_index_a][column_index_shared] > 0
                          and
                          matrix_in_question[row_index_b][column_index_shared] > 0)
    both_rows_negative = (matrix_in_question[row_index_a][column_index_shared] < 0
                          and
                          matrix_in_question[row_index_b][column_index_shared] < 0)

    if both_rows_positive or both_rows_negative:
        print(tab_amount + "\t\t\t",
              f"They were either both positive or negative. So i set row {row_index_b} * -1")
        scale_row_from_number(matrix=matrix_in_question, row_in_question=row_index_b, number=-1,
                              tab_amount=tab_amount + "\t\t\t")
        determinant_operation_string_values_list.append("-1")
        determinant_operation_numeric_values_list.append(-1)
    else:
        print(tab_amount + "\t\t\t", "they were opposite signs so no operation needed.")

    :param column_index_shared: the index at which the row's columns are being compared
    :param row_index_a: row a in the matrix_in_question :-)
    :param row_index_b: row b in the matrix_in_question :-)
    :param matrix_in_question: matrix of reasonable size
    :param tab_amount: variations of "\t"
    :return: if row a and row b in matrix in question are both + or -. then it scales row b by -1. if not then it does nothing.
    """
    print(tab_amount,"REF_both_pos_or_neg_helper")
    tab_amount += "\t"
    print(tab_amount,f"are row {row_index_a} and row {row_index_b} both positive or both negative?")
    tab_amount += "\t"

    both_rows_positive_bool = \
        (
                matrix_in_question[row_index_a][column_index_shared] > 0
                and
                matrix_in_question[row_index_b][column_index_shared] > 0
        )
    both_rows_negative_bool = \
        (
                matrix_in_question[row_index_a][column_index_shared] < 0
                and
                matrix_in_question[row_index_b][column_index_shared] < 0
        )
    if both_rows_positive_bool or both_rows_negative_bool:
        print(tab_amount,f"either row {row_index_a} or row {row_index_b} were both positive or both negative")
        scale_row_from_number(matrix=matrix_in_question,row_in_question=row_index_b,number=-1,tab_amount=tab_amount)

    return matrix_in_question