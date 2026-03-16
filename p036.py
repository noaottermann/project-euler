from euler import run
from utils import *

# Euler Problem 36

def solve():
    total = 0
    for n in range(1, 10**6):
        if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
            total += n
    return total

if __name__ == '__main__':
    run(solve, problem_id=36)