from euler import run
from utils import *

# Euler Problem 69

def solve():
    # We want to maximize n/phi(n) where phi(n) is the number of integers less than n that are coprime to n.
    # If n = p1^k1 * p2^k2 * ... * pm^km, then phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm)
    # Therefore, n/phi(n) = 1 / ((1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm))
    # To maximize n/phi(n), we need to minimize the product (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm)
    # This means we need to include as many distinct prime factors as possible, starting from the smallest primes.
    # We will keep multiplying the smallest primes until the product exceeds 10^6.

    product = 1
    n = 1
    # 100 is an arbitrary limit for the sieve, we will break out of the loop once the product exceeds 10^6
    for prime in sieve_of_eratosthenes(100):
        if product * prime > 10**6:
            break
        product *= prime
        n *= prime
    return n

if __name__ == '__main__':
    run(solve, problem_id=69)