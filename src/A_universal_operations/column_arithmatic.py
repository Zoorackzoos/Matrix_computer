def multiply_column_a_and_column_b(column_a, column_b, tab_amount="\t"):
    """
    these matrices ARE NOT nested. they're lists of numbers only.
    so hlep me if you put in
    [
        [n]
    ]
    i'll find you and kiss you hehe :-3

    :param column_a:
    :param column_b:
    :param tab_amount:
    :return:
    """
    print(tab_amount, "multiply_columns_only")
    tab_amount += "\t"

    results_list = []

    column_a_length = len(column_a)
    column_b_length = len(column_b)

    if(isinstance(column_a[0], list)):
        exit("column_a is a list of lists. not cool bro")

    if (isinstance(column_b[0], list)):
        exit("column_a is a list of lists. not cool bro")

    if(column_a_length != column_b_length):
        print(tab_amount,column_a_length)
        print(tab_amount,column_b_length)
        exit("the length of column_a and column_b are not equal")

    for i in range(column_a_length):
        product = column_a[i] * column_b[i]
        results_list.append(product)

    return results_list

def get_sum_of_column(column,tab_amount="\t"):
    print(tab_amount, "get_sum_of_column")
    tab_amount += "\t"

    sum = 0
    for i in range(len(column)):
        sum += column[i]

    return sum

def multiply_column_and_scaler(column, scaler, tab_amount="\t"):
    print(tab_amount, "multiply_column_and_scaler")
    tab_amount += "\t"

    result_column = []

    for i in range(len(column)):
        result_column.append(column[i] * scaler)

    return result_column

def add_column_a_and_column_b(column_a, column_b, tab_amount="\t"):
    print(tab_amount, "add_column_a_and_column_b")
    tab_amount += "\t"

    added_column = []

    for i in range(len(column_a)):
        print(tab_amount,i)
        print(tab_amount,column_a[i])
        print(tab_amount,column_b[i])
        print()
        added_column.append(column_a[i] + column_b[i])

    return added_column