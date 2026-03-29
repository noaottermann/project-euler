from euler import run
from utils import *

# Euler Problem 65

def solve():
    # The nth term of the sequence is given by a(n) = 1 if n % 3 != 0 else 2 * (n // 3) for n >= 2
    terms = [2] + [1 if n % 3 != 0 else 2 * (n // 3) for n in range(2, 101)]
    numerator = 1
    denominator = terms[-1]
    for term in terms[:-1][::-1]:
        numerator, denominator = denominator, term * denominator + numerator
    return sum(int(digit) for digit in str(denominator))

if __name__ == '__main__':
    run(solve, problem_id=65)