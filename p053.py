from euler import run
from utils import *

# Euler Problem 53

def solve():
    count = 0
    already_counted = set()
    for n in range(1, 101):
        for r in range(1, n + 1):
            if nCr(n, r) > 10**6:
                if (n, r) not in already_counted:
                    already_counted.add((n, r))
                    count += 1
                    if n - r != r:
                        already_counted.add((n, n - r))
                        count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=53)