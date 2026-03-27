from euler import run
from utils import *

# Euler Problem 63

def solve():
    total = 0
    n = 1
    while True:
        count = 0
        for p in range(1, 10):
            if len(str(p**n)) == n:
                count += 1
        if count == 0:
            break
        total += count
        n += 1
    return total

if __name__ == '__main__':
    run(solve, problem_id=63)