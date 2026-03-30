from euler import run
from utils import *
from math import log

# Euler Problem 99

def solve():
    with open('p099_base_exp.txt') as f:
        lines = f.read().strip().splitlines()
    max_value = 0
    max_index = 0
    for i, line in enumerate(lines):
        base, exp = map(int, line.split(','))
        value = exp * log(base)
        if value > max_value:
            max_value = value
            max_index = i + 1
    return max_index

if __name__ == '__main__':
    run(solve, problem_id=99)