from euler import run
from utils import *

# Euler Problem 112

def solve():
    bouncy_count = 0
    n = 1
    while True:
        if is_bouncy(n):
            bouncy_count += 1
        if bouncy_count/n == 0.99:
            return n
        n += 1

if __name__ == '__main__':
    run(solve, problem_id=112)