from fractions import Fraction

def float_to_fraction_numerical(x, max_denominator=1000000):
    frac = Fraction(x).limit_denominator(max_denominator)
    return frac

def float_to_fraction_string(x, max_denominator=1000000):
    frac = Fraction(x).limit_denominator(max_denominator)
    return f"{frac.numerator}/{frac.denominator}"