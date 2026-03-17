from euler import run
from utils import *

# Euler Problem 43

def solve():
    pandigital_numbers = generate_permutations("".join(str(i) for i in range(0, 10)))
    total = 0
    for num in pandigital_numbers:
        if (int(num[1:4]) % 2 == 0 and
            int(num[2:5]) % 3 == 0 and
            int(num[3:6]) % 5 == 0 and
            int(num[4:7]) % 7 == 0 and
            int(num[5:8]) % 11 == 0 and
            int(num[6:9]) % 13 == 0 and
            int(num[7:10]) % 17 == 0):
            total += int(num)
    return total


if __name__ == '__main__':
    run(solve, problem_id=43)