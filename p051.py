from euler import run
from utils import *

# Euler Problem 51

def solve():
    # n is the number of digits in the prime, d is the digit to be replaced, p is the prime number
    # We look for primes with at least 3 occurrences of the same digit, and then we replace that digit with all possible digits and count how many of those are prime. If we find a prime that has exactly 8 such replacements, we return it
    for n in range(1, 10):
        for d in range(10):
            for p in sieve_of_eratosthenes(10**n, 10**(n+1)):
                s = str(p)
                if s.count(str(d)) >= 3:
                    c = 0
                    for i in range(10):
                        if str(i) == str(d):
                            q = s
                        else:
                            q = s.replace(str(d), str(i))
                        if q[0] != '0' and is_prime(int(q)):
                            c += 1
                    if c == 8:
                        return p

if __name__ == '__main__':
    run(solve, problem_id=51)