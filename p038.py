from euler import run
from utils import *

# Euler Problem 38

def solve():
    # n > 1 because we need at least two multiples to concatenate
    # 10**(9 // n) is the largest integer i such that the concatenation of i, 2*i, ..., n*i has at most 9 digits
    maximum_pandigital = 0
    for n in range(2, 10):
        for i in range(1, 10**(9 // n)):
            pandigital = ''.join(str(i * j) for j in range(1, n + 1))
            if len(pandigital) == 9 and set(pandigital) == set('123456789'):
                maximum_pandigital = max(maximum_pandigital, int(pandigital))
    return maximum_pandigital
            
if __name__ == '__main__':
    run(solve, problem_id=38)