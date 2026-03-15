from euler import run
from utils import *

# Euler Problem 9

def solve():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

if __name__ == '__main__':
    run(solve, problem_id=9)