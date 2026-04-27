import sys


def get_dot_product(matrix_a, matrix_b, tab_amount="\t"):
    """
    vectors? matrices? whatever

    a_1 * b_1 + a_2 * b_2 + ....
        keeps going and going.
    and you end up with a "scaler"
        or in plain english , instead of shithead terms. a "number"

    the size of the matrixes doesn't matter as long as they're the same size.
    if they're not the funciton says "wtf bro" and stops.

    :param matrix_a: a matrix of reasonable size
    :param matrix_b: a matrix of reasonable size
    :param tab_amount: variations of "\t"
    :return: a number that's the dot product of the 2 matrices
    """
    print(tab_amount,"get_dot_product")
    tab_amount += "\t"

    # if i catch you with matrices with different dimensions. i'll get ya.
    if (len(matrix_a) != len(matrix_b)) or (len(matrix_a[0]) != len(matrix_b[0])):
        print(tab_amount,"matrix_a and matrix_b are not the same length. wtf bro.")
        print(tab_amount,len(matrix_a))
        print(tab_amount,len(matrix_b))
        sys.exit("matrix_a and matrix_b are not the same length. wtf bro.")

    # multiply, add that to the sum, then do it again until we don't have terms anymore
    x_dimension_both = len(matrix_a[0])
    y_dimension_both = len(matrix_a)

    dot_product_total = 0
    print(tab_amount,"dot_product_total -> ",dot_product_total)

    print(tab_amount,"x_dimension_both -> ",x_dimension_both)
    print(tab_amount,"y_dimension_both -> ",y_dimension_both)
    print(tab_amount,"start of loop")

    for x in range(y_dimension_both):
        print(tab_amount+"\t","x -> ",x)
        for y in range(x_dimension_both):
            print(tab_amount+"\t\t","y -> ",y)
            print(tab_amount+"\t\t","matrix_a[i][j] -> ",matrix_a[x][y])
            print(tab_amount+"\t\t","matrix_b[i][j] -> ",matrix_b[x][y])
            dot_product_total += matrix_a[x][y] * matrix_b[x][y]
            print(tab_amount+"\t\t","dot_product_total -> ", dot_product_total)
    print()

    print(tab_amount,"dot_product_total -> ",dot_product_total)

    return dot_product_total


if __name__ == "__main__":
    """
    matrix_a = \
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    matrix_b = \
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    tab_amount = "\t"

    get_dot_product(matrix_a, matrix_b, tab_amount)
    """

    """
    x = \
        [
            [-5],
            [-2],
            [0]
        ]
    y = \
        [
            [-3],
            [5],
            [-3]
        ]
    """
    x = \
    [
        [-8],
        [2],
        [-2],
        [0]
    ]
    y = \
    [
        [-7],
        [1],
        [11],
        [-3]
    ]
    tab_amount = "\t"
    variable_lol = get_dot_product(matrix_a=x, matrix_b=y, tab_amount=tab_amount)
    print(variable_lol)
