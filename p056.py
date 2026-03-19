from euler import run
from utils import *

# Euler Problem 56

def solve():
    return max(sum_digits(a**b) for a in range(100) for b in range(100))

if __name__ == '__main__':
    run(solve, problem_id=56)