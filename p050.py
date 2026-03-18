from euler import run
from utils import *

# Euler Problem 50

def solve():
    limit = 10**6
    primes = list(sieve_of_eratosthenes(limit))

    longest_length = 0
    longest_prime = 0

    for i in range(len(primes)):
        for j in range(i + longest_length, len(primes)):
            s = sum(primes[i:j])
            if s >= limit:
                break
            if s in primes:
                longest_length = j - i
                longest_prime = s

    return longest_prime

if __name__ == '__main__':
    run(solve, problem_id=50)