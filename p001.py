from euler import run
from utils import *

# Euler Problem 1

def solve():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

if __name__ == '__main__':
    run(solve, problem_id=1)