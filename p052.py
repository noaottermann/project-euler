from euler import run
from utils import *

# Euler Problem 52

def solve():
    for n in range(1, 1000000):
        if all(is_permutation(n, n * i) for i in range(2, 7)):
            return n

if __name__ == '__main__':
    run(solve, problem_id=52)