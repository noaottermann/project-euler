from euler import run
from utils import *

# Euler Problem 47

def solve():
    # 210 is the smallest number that can be expressed as the product of 4 distinct primes
    # We need to optimize the search by remembering numbers that doesn't have 4 distinct prime factors so we can skip them
    n = 2*3*5*7
    invalid = set()
    while True:
        for i in range(n, n+4):
            if i in invalid:
                n = i + 1
                break
            if distinct_prime_factors(i) != 4:
                invalid.add(i)
                n = i + 1
                break
        else:
            return n

if __name__ == '__main__':
    run(solve, problem_id=47)