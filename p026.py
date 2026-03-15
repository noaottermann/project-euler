from euler import run
from utils import *

# Euler Problem 26

def solve():
    max_length = 0
    result = 0
    for d in range(1, 1000):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            result = d
    return result

if __name__ == '__main__':
    run(solve, problem_id=26)