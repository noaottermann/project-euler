from euler import run
from utils import *

# Euler Problem 16

def solve():
    return sum(int(digit) for digit in str(2**1000))

if __name__ == '__main__':
    run(solve, problem_id=16)