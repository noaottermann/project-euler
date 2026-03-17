from euler import run
from utils import *

# Euler Problem 41

def solve():
    for n in range(9, 0, -1):
        pandigital_numbers = generate_permutations("".join(str(i) for i in range(1, n + 1)))
        pandigital_numbers.sort(reverse=True)
        for num in pandigital_numbers:
            if is_prime(int(num)):
                return num

if __name__ == '__main__':
    run(solve, problem_id=41)