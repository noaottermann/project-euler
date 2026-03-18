from euler import run
from utils import *

# Euler Problem 45

def solve(): 
    # n = 143 is the first triangle number that is also pentagonal and hexagonal, so we start from there
    n = 144
    while True:
        n += 1
        hexagonal_number = n * (2 * n - 1)
        if is_pentagonal(hexagonal_number) and is_triangular(hexagonal_number):
            return hexagonal_number

if __name__ == '__main__':
    run(solve, problem_id=45)