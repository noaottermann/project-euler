from euler import run
from utils import *

# Euler Problem 58

def solve():
    n = 1
    total = 1
    primes = 0
    while True:
        n += 2
        total += 4
        for i in range(4):
            if is_prime(n**2 - i*(n-1)):
                primes += 1
        if primes / total < 0.10:
            return n

if __name__ == '__main__':
    run(solve, problem_id=58)