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
                if any(not are_concat_primes(x, c) for x in (a, b)):
                    continue
                for d in primes:
                    if d <= c:
                        continue
                    if any(not are_concat_primes(x, d) for x in (a, b, c)):
                        continue
                    for e in primes:
                        if e <= d:
                            continue
                        if any(not are_concat_primes(x, e) for x in (a, b, c, d)):
                            continue
                        return a + b + c + d + e

if __name__ == '__main__':
    run(solve, problem_id=60)