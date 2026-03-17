from euler import run
from utils import *

# Euler Problem 44

def solve():
    # 10000 is 
    pentagonal_numbers = set()
    for n in range(1, 10000):
        pentagonal_number = n * (3 * n - 1) // 2
        pentagonal_numbers.add(pentagonal_number)
    min_diff = float('inf')
    for p1 in pentagonal_numbers:
        for p2 in pentagonal_numbers:
            if p1 != p2 and (p1 + p2) in pentagonal_numbers and abs(p1 - p2) in pentagonal_numbers:
                min_diff = min(min_diff, abs(p1 - p2))
    return min_diff

if __name__ == '__main__':
    run(solve, problem_id=44)