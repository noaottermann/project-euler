from euler import run
from utils import *

# Euler Problem 33

def solve():
    curious_fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if is_curious_fraction(numerator, denominator):
                curious_fractions.append((numerator, denominator))
    product_numerator = 1
    product_denominator = 1
    for numerator, denominator in curious_fractions:
        product_numerator *= numerator
        product_denominator *= denominator
    common_divisor = gcd(product_numerator, product_denominator)
    simplified_denominator = product_denominator // common_divisor
    return simplified_denominator

if __name__ == '__main__':
    run(solve, problem_id=33)