from euler import run
from utils import *

# Euler Problem 39

def solve():
    # p = a + b + c and a^2 + b^2 = c^2
    # We can rewrite the second equation as a^2 + b^2 = (p - a - b)^2
    # b goes from a to (p - a) // 2 because b < c => b < p - a - b => 2b < p - a => b < (p - a) // 2
    max_solutions = 0
    max_p = 0
    for p in range(1, 1001):
        solutions = 0
        for a in range(1, p):
            for b in range(a, (p - a) // 2 + 1):
                if a**2 + b**2 == (p - a - b)**2:
                    solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p
    return max_p

if __name__ == '__main__':
    run(solve, problem_id=39)