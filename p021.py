from euler import run
from utils import *

# Euler Problem 21

def solve():
    total = 0
    for n in range(1, 10000):
        m = sum(proper_divisors(n))
        if m != n and sum(proper_divisors(m)) == n:
            total += n
    return total

if __name__ == '__main__':
    run(solve, problem_id=21)