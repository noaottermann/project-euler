from euler import run
from utils import *

# Euler Problem 92

def solve():
    cache = [0] * (9 * 9 * 7 + 1)
    cache[1] = 1
    cache[89] = 89

    count = 0
    for n in range(1, 10**7):
        chain = []
        m = n
        while m != 1 and m != 89 and (m >= len(cache) or cache[m] == 0):
            chain.append(m)
            m = sum_squares_digits(m)

        result = 89 if m == 89 or (m < len(cache) and cache[m] == 89) else 1
        for value in chain:
            if value < len(cache):
                cache[value] = result

        if result == 89:
            count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=92)