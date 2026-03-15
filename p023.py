from euler import run
from utils import *

# Euler Problem 23

def solve():
    # All integers greater than 28123 can be written as the sum of two abundant numbers
    limit = 28123
    abundant_numbers = [n for n in range(1, limit + 1) if is_abundant(n)]
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])
    return sum(n for n in range(1, limit + 1) if n not in abundant_sums)

if __name__ == '__main__':
    run(solve, problem_id=23)