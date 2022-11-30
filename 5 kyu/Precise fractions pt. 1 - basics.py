from fractions import Fraction
Fraction.to_decimal = lambda f: float(f.numerator) / f.denominator
simple_fraction = Fraction.__str__
def mixed_fraction(f):
    n, d, s = abs(f.numerator), f.denominator, simple_fraction(f)
    return s.replace(str(n), '%d %d' % divmod(n, d), 1) if 1 < d < n else s
Fraction.__str__ = mixed_fraction