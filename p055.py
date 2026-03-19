from euler import run
from utils import *

# Euler Problem 55

def solve():
    count = 0
    for n in range(1, 10000):
        if is_lychrel(n, 50):
            count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=55)