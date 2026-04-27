from pandas.core.dtypes.inference import is_integer

def get_decimal_length(number):
    """
    Calculates the number of digits after the decimal point in a float.

    Args:
        number (float): The floating-point number.

    Returns:
        int: The number of digits after the decimal point.
    """
    s = str(number)
    if '.' in s:
        return len(s) - s.find('.') - 1
    else:
        return 0

#made of sin
def convert_to_divided_by_sqrt(number,tab_amount="\t", tolerance=1e-6, max_check=10000):
    """
    turns shitty irrational numbers into their fraction counterparts so you can read them.

    :param number: a number of any type. int, float, double whatever
    :param tab_amount: variations of "\t"
    :param tolerance: used to judge how you want your number fixed to be sqrt applicable. keep the default value.
    :param max_check: idfk dude. keep the default value.
    :return:
    """
    print(f"{tab_amount}convert_to_divided_by_sqrt")
    if is_integer(number):
        print(f"{tab_amount}\tit's a integer so there's no sqrt risk")
        return None
    if get_decimal_length(number) <= 3:
        print(f"{tab_amount}\tthe decimal length of {number} is too small")
    else:
        print(f"{tab_amount}\tit's not a integer. maybe a sqrt.")
        for a in range(1, max_check):
            for b in range(1, max_check):
                candidate = a / (b ** 0.5)
                if abs(candidate - number) < tolerance:
                    return f"{a}/sqrt({b})"
        return number

if __name__ == "__main__":
    weird_sum = 1.6 + 3.2
    print( convert_to_divided_by_sqrt(number=weird_sum, tab_amount="\t") )