from euler import run
from utils import *

# Euler Problem 46

def solve():
    n = 9
    while True:
        n += 2
        if is_prime(n):
            continue
        found = False
        for p in sieve_of_eratosthenes(n):
            if is_perfect_square((n - p) // 2):
                found = True
                break
        if not found:
            return n
        

if __name__ == '__main__':
    run(solve, problem_id=46)