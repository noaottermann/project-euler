from euler import run
from utils import *

# Euler Problem 4

def solve():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product
    return max_palindrome

if __name__ == '__main__':
    run(solve, problem_id=4)