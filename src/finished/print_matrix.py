from src.finished.float_to_fraction_string import float_to_fraction_string

def print_matrix(matrix, tab_amount="\t"):
    print(tab_amount,"print_matrix")
    return_string = ""
    for row in matrix:
        print(tab_amount+"\t",row)

def print_matrix_frac(matrix, tab_amount="\t"):
    print(tab_amount, "print_matrix_frac")
    for row in matrix:
        for element in row:
            print(tab_amount+"\t", float_to_fraction_string(element), end="")
        print()