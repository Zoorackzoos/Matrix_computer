from src.A_universal_operations.display.float_to_fraction_string import float_to_fraction_string


def column_float_to_fraction_string(column, tab_amount="\t"):
    print(tab_amount,"column_float_to_fraction_string")
    tab_amount += "\t"
    result_matrix = []

    for i in range(len(column)):
        result_matrix.append(float_to_fraction_string(column[i]))

    return result_matrix