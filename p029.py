from euler import run
from utils import *

# Euler Problem 29

def solve():
    s = set()
    for a in range(2, 101):
        for b in range(2, 101):
            s.add(a ** b)
    return len(s)

if __name__ == '__main__':
    run(solve, problem_id=29)