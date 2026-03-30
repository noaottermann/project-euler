from euler import run
from utils import *

# Euler Problem 79

def solve():
    with open('p079_keylog.txt') as f:
        keylog = [to_digits(line.strip()) for line in f]
    digits = set()
    for code in keylog:
        digits.update(code)
    digits = sorted(digits)
    for perm in permutations(digits):
        if all(is_subsequence(code, perm) for code in keylog):
            return int(''.join(map(str, perm)))

if __name__ == '__main__':
    run(solve, problem_id=79)