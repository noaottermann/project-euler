from euler import run
from utils import *

# Euler Problem 13

def solve():
    numbers = [line.strip() for line in open('p013_numbers.txt')]
    total = sum(int(num) for num in numbers)
    return str(total)[:10]

if __name__ == '__main__':
    run(solve, problem_id=13)