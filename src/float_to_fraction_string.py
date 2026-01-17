from fractions import Fraction

def float_to_fraction_string(value: float, max_denominator: int = 20):
    """
    Convert a float into a fraction string if it can be represented cleanly.

    Parameters
    ----------
    value : float
        The floating-point number to convert.

    max_denominator : int, optional (default=20)
        The largest denominator allowed when approximating the fraction.
        Smaller values = stricter matching.
        Larger values = more aggressive fraction guessing.

    Returns
    -------
    str or float
        A string like "1/3", "-5/4", or "2" if a clean fraction is found.
        Otherwise, returns the original float unchanged.

    Notes
    -----
    - Negative values are fully supported.
    - If the fraction simplifies to a whole number, it is returned as "n".
    - If the denominator exceeds `max_denominator`, the float is returned.
    """

    if value == "|":
        return value
    # Handle exact integers immediately
    if value.is_integer():
        return str(int(value))

    try:
        frac = Fraction(value).limit_denominator(max_denominator)
    except Exception:
        return value

    # If the approximation is too imprecise, reject it
    if abs(float(frac) - value) > 1e-9:
        return value

    numerator, denominator = frac.numerator, frac.denominator

    if denominator == 1:
        return str(numerator)

    return f"{numerator}/{denominator}"
