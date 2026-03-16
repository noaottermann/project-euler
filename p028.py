from euler import run
from utils import *

# Euler Problem 28

def solve():
    total = 1
    n = 1
    for i in range(1, 1001, 2):
        for _ in range(4):
            n += i
            total += n
    return total


if __name__ == '__main__':
    run(solve, problem_id=28)