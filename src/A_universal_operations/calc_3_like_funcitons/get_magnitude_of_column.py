import math


def get_magnitude_of_column(column, tab_amount="\t"):
    print(tab_amount,"get_magnitude_of_column")
    tab_amount += "\t"

    magnitude = 0

    for number in column:
        magnitude += math.pow(number,2)

    return math.sqrt(magnitude)