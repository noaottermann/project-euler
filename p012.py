from euler import run
from utils import *

# Euler Problem 12

def solve():
    n = 1
    while True:
        triangular = n * (n + 1) // 2
        if count_divisors(triangular) > 500:
            return triangular
        n += 1

if __name__ == '__main__':
    run(solve, problem_id=12)