from euler import run
from utils import *

# Euler Problem 97

def solve():
    mod = 10**10
    power = pow(2, 7830457, mod)
    result = (28433 * power + 1) % mod
    return result

if __name__ == '__main__':
    run(solve, problem_id=97)