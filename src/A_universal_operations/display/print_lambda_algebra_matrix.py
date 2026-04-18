import sys


def print_lambda_algebra_matrix(lambda_algebra_matrix, tab_amount = "\t"):
    """
    this come sin the form:
    equation_1 = \
        [
            matrix_with_lambdas[0][0]
            , "("
            , "(" , matrix_with_lambdas[1][1] , "*" , matrix_with_lambdas[2][2] , ")"
            , "-"
            , "(" , matrix_with_lambdas[1][2] , "*" , matrix_with_lambdas[2][1] , ")"
            , ")"
        ]
    IT HAS TO BE 3 X 3 OR THIS WILL NOT WORK

    :param lambda_algebra_matrix:
    :param tab_amount:
    :return:
    """
    print(tab_amount,"print_lambda_algebra_matrix")
    tab_amount += "\t"
    sys.stdout.write(tab_amount)
    for element in lambda_algebra_matrix:
        sys.stdout.write(str(element)+" ")
    print()

if __name__ == "__main__":
    tab_amount = "\t"

    matrix_with_lambdas = \
        [
            [[37, "-λ"], [28, ""], [-160, ""]],
            [[17, ""], [19, "-λ"], [-55, ""]],
            [[16, ""], [14, ""], [-48, "-λ"]]
        ]

    equation_1 = \
        [
            matrix_with_lambdas[0][0]
            , "("
            , "(", matrix_with_lambdas[1][1], "*", matrix_with_lambdas[2][2], ")"
            , "-"
            , "(", matrix_with_lambdas[1][2], "*", matrix_with_lambdas[2][1], ")"
            , ")"
        ]

    print_lambda_algebra_matrix(lambda_algebra_matrix=equation_1,tab_amount=tab_amount)