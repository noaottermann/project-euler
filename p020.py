from euler import run
from utils import *

# Euler Problem 20

def solve():
    return sum_digits(factorial(100))

if __name__ == '__main__':
    run(solve, problem_id=20)