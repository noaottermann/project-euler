from euler import run
from utils import *

# Euler Problem 30

def solve():
    # We are looking for numbers that can be written as the sum of fifth powers of their digits.
    # The upper limit can be determined by noting that 9^5 * 6 = 354294, so we only need to check numbers up to that point.
    # Because 7*9^5 is a 6-digit number, we can be sure that any number with more than 6 digits cannot be written as the sum of fifth powers of its digits.
    total = 0
    for n in range(2, 354295):
        s = sum(int(d) ** 5 for d in str(n))
        if s == n:
            total += n
    return total

if __name__ == '__main__':
    run(solve, problem_id=30)