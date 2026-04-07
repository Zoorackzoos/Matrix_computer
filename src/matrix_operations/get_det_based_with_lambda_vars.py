from src.display.print_matrix import *
from src.display.float_to_fraction_string import *
from src.display.print_lambda_algebra_matrix import *

def get_det_based_with_lambda_vars_in_3x3_matrix(matrix_with_lambdas, tab_amount ="\t"):
    """

    :param matrix_with_lambdas: lists that contain lists that contain
     lists with only 2 elements which represent the number and then the
     variable, if there is no variable then it is just ""
     HAS TO BE 3 X 3 OR THIS WILL NOT WORK.

    :param tab_amount:
    :return:
    """
    print(tab_amount,"get_det_based_with_lambda_vars_in_3x3_matrix")
    tab_amount += "\t"

    print_matrix(matrix_in_question=matrix_with_lambdas,tab_amount=tab_amount)

    """
    craft equation 1, 2 and 3. 
    these are the polynomials you will simply later
    """
    equation_1_original = \
        [
            matrix_with_lambdas[0][0],
            "(",
                "(",
                    matrix_with_lambdas[1][1],
                    "*",
                    matrix_with_lambdas[2][2],
                ")",
                "-",
                "(",
                    matrix_with_lambdas[1][2],
                    "*",
                    matrix_with_lambdas[2][1],
                ")",
            ")"
        ]
    equation_2_original = \
        [
            matrix_with_lambdas[0][1],
            "(",
                "(",
                    matrix_with_lambdas[1][0],
                    "*",
                    matrix_with_lambdas[2][2],
                ")",
                "-",
                "(",
                    matrix_with_lambdas[1][2],
                    "*",
                    matrix_with_lambdas[2][0],
                ")",
            ")"
        ]
    equation_3_original = \
        [
            matrix_with_lambdas[0][2],
            "(",
                "(",
                    matrix_with_lambdas[1][0],
                    "*",
                    matrix_with_lambdas[2][1],
                ")",
                "-",
                "(",
                    matrix_with_lambdas[1][1],
                    "*",
                    matrix_with_lambdas[2][0],
                ")",
            ")"
        ]

    print_lambda_algebra_matrix(lambda_algebra_matrix=equation_1_original,tab_amount=tab_amount)
    print_lambda_algebra_matrix(lambda_algebra_matrix=equation_2_original,tab_amount=tab_amount)
    print_lambda_algebra_matrix(lambda_algebra_matrix=equation_3_original,tab_amount=tab_amount)

    """
    we have the equations now. 
    we have to simplify what's inside them
    """
    lambda_algebra_operation(lambda_list_a=equation_1_original[3], lambda_list_b=equation_1_original[5], title_of_operation="equation 1 , multiplant 1", operation_string=equation_2_original[4])

    exit(999)

def lambda_algebra_operation(lambda_list_a, lambda_list_b, operation_string, title_of_operation = "untitled", tab_amount = "\t"):
    print(tab_amount,"lambda_algebra_operation")
    tab_amount += "\t"
    print(tab_amount,title_of_operation)
    print()
    tab_amount += "\t"

    print(tab_amount,lambda_list_a)
    print(tab_amount,operation_string)
    print(tab_amount,lambda_list_b)
    print()

    """
        19      -λ
    -48 x       48λ
    -λ  -19λ    λ^2
    """
    if (lambda_list_a[1][1] != ""
        and lambda_list_b[1][1] != ""
        and lambda_list_a[1][1] == lambda_list_b[1][1]):
        #TODO: finish this function. i'm too geeked to proceed.

    exit(999)

if __name__ == "__main__":
    tab_amount = "\t"
    """
    this is different from other matrix's i have configured for this project
    they're very unstandardized.
    so it's going to be very singular use.
    """
    matrix_with_lambdas = \
        [
            [ [37,[-1,"λ",1]] , [28,[0,"",0]] , [-160,[0,"",0]] ],
            [ [17,[0,"",0]] , [19,[-1,"λ",1]] , [-55,[0,"",0]] ],
            [ [16,[0,"",0]] , [14,[0,"",0]] , [-48,[-1,"λ",1]] ]
        ]
    get_det_based_with_lambda_vars_in_3x3_matrix(matrix_with_lambdas=matrix_with_lambdas,tab_amount=tab_amount)