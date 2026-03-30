from euler import run
from utils import *

# Euler Problem 8

def solve():
    digits = ''.join([line.strip() for line in open('p008_1000_digits.txt')])
    max_product = 0
    for i in range(len(digits) - 13):
        product = 1
        for j in range(13):
            product *= int(digits[i + j])
        max_product = max(max_product, product)
    return max_product

if __name__ == '__main__':
    run(solve, problem_id=8)