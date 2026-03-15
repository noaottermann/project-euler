from euler import run
from utils import *

# Euler Problem 2

def solve():
    a, b = 1, 2
    total = 0
    while a <= 4*10**6:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

if __name__ == '__main__':
    run(solve, problem_id=2)