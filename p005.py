from euler import run
from utils import *

# Euler Problem 5

def solve():
    return lcm(*range(2, 21))

if __name__ == '__main__':
    run(solve, problem_id=5)