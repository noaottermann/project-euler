from euler import run
from utils import *

# Euler Problem 10

def solve():
    limit = 2*10**6
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return sum(i for i in range(limit) if sieve[i])

if __name__ == '__main__':
    run(solve, problem_id=10)