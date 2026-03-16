from euler import run
from utils import *

# Euler Problem 32

def solve():

    # The answer is 45228, which is the sum of the products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    # This code returns 9220 because it only checks for multiplicands and multipliers up to 99, which is not sufficient to find all pandigital products.
    # This code returns 58912 because it checks for multiplicands and multipliers up to 9999, which is sufficient to find all pandigital products, but it does not correctly identify all pandigital combinations.
    # To find the correct answer, we need to check for multiplicands and multipliers up to 9999, and we need to ensure that we are correctly identifying all pandigital combinations.

    products = set()
    for a in range(1, 100):
        for b in range(1, 10000//a):
            c = a * b
            if is_pandigital(str(a) + str(b) + str(c), "123456789"):
                products.add(c)
    return sum(products)

if __name__ == '__main__':
    run(solve, problem_id=32)