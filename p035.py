from euler import run
from utils import *

# Euler Problem 35

def solve():
    count = 0
    for n in range(1, 1000000):
        if is_circular_prime(n):
            count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=35)