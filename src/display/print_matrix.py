from src.display.float_to_fraction_string import float_to_fraction_string

def print_matrix(matrix_in_question, tab_amount="\t"):
    print(tab_amount,"print_matrix")
    for row in matrix_in_question:
        print(tab_amount+"\t",row)

def print_matrix_frac(matrix_in_question, tab_amount="\t"):
    print(tab_amount, "print_matrix_frac")
    for row in matrix_in_question:
        for element in row:
            print(tab_amount+"\t", float_to_fraction_string(element), end="")
        print()