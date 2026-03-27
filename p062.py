from euler import run
from utils import *

# Euler Problem 62

def solve():
    cubes = {}
    n = 1
    while True:
        c = n**3
        key = ''.join(sorted(str(c)))
        cubes.setdefault(key, []).append(c)
        if len(cubes[key]) == 5:
            return min(cubes[key])
        n += 1

if __name__ == '__main__':
    run(solve, problem_id=62)