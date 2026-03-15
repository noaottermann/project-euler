from euler import run
from utils import *

# Euler Problem 7

def solve():
    n = 10001
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == '__main__':
    run(solve, problem_id=7)