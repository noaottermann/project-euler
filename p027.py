from euler import run
from utils import *

# Euler Problem 27

def solve():
    def f(n, a, b):
        return n**2 + a*n + b
    
    max_length = 0
    product = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(f(n, a, b)):
                n += 1
            if n > max_length:
                max_length = n
                product = a * b
    return product

if __name__ == '__main__':
    run(solve, problem_id=27)