from euler import run
from utils import *

# Euler Problem 37

def solve():
    # We start from 11 because single-digit primes are not considered truncatable primes.
    # A truncatable prime is mandatory to be odd, because if it ends with an even digit, it cannot be prime (except for 2, which is not considered truncatable).
    truncatable_primes = []
    n = 11
    while len(truncatable_primes) < 11:
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
        n += 2
    return sum(truncatable_primes)

if __name__ == '__main__':
    run(solve, problem_id=37)