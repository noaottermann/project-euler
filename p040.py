from euler import run
from utils import *

# Euler Problem 40

def solve():
    concatenated = ''.join(str(i) for i in range(1, 1000000))
    product = 1
    for i in range(7):
        product *= int(concatenated[10**i - 1])
    return product

if __name__ == '__main__':
    run(solve, problem_id=40)