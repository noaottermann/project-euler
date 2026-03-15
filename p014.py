from euler import run
from utils import *

# Euler Problem 14

def solve():
    maximum_length = 0
    number_with_max_length = 0
    for i in range(1, 10**6):
        length = collatz_length(i)
        if length > maximum_length:
            maximum_length = length
            number_with_max_length = i
    return number_with_max_length

if __name__ == '__main__':
    run(solve, problem_id=14)