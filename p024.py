from euler import run
from utils import *

# Euler Problem 24

def solve():
    permutations = generate_permutations('0123456789')
    permutations.sort()
    return permutations[10**6 - 1]

if __name__ == '__main__':
    run(solve, problem_id=24)