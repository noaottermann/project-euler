from euler import run
from utils import *

# Euler Problem 25

def solve():
    a, b = 1, 1
    index = 2
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) >= 1000:
            return index

if __name__ == '__main__':
    run(solve, problem_id=25)