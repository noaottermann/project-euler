from euler import run
from utils import *

# Euler Problem 34

def solve():
    # The upper limit is 7 * 9! because 9! is the largest factorial for a single digit and we can have at most 7 digits (since 8 * 9! is still a 7-digit number).
    limit = 7 * factorial(9)
    total = 0
    for n in range(10, limit):
        if n == sum(factorial(int(digit)) for digit in str(n)):
            total += n
    return total

if __name__ == '__main__':
    run(solve, problem_id=34)