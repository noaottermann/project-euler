from euler import run
from utils import *

# Euler Problem 64

def solve():
    count = 0
    for n in range(1, 10000):
        if len(period_root_continued_fraction(n)) % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=64)