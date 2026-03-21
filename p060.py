from euler import run
from utils import *

# Euler Problem 60

def solve():
    primes = sieve_of_eratosthenes(10**4)
    for a in primes:
        for b in primes:
            if b <= a:
                continue
            if not are_concat_primes(a, b):
                continue
            for c in primes:
                if c <= b:
                    continue
                if not (are_concat_primes(a, c) and are_concat_primes(b, c)):
                    continue
                for d in primes:
                    if d <= c:
                        continue
                    if not (are_concat_primes(a, d) and are_concat_primes(b, d) and are_concat_primes(c, d)):
                        continue
                    for e in primes:
                        if e <= d:
                            continue
                        if not (are_concat_primes(a, e) and are_concat_primes(b, e) and are_concat_primes(c, e) and are_concat_primes(d, e)):
                            continue
                        return a + b + c + d + e

if __name__ == '__main__':
    run(solve, problem_id=60)