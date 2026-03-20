from euler import run
from utils import *

# Euler Problem 57

def solve():
    # a is the numerator, b is the denominator
    # Explanation:
    # The nth expansion can be found by the following recurrence:
    # 1 + 1/(1 + a(n)/b(n)) = 1 + b(n)/(a(n) + b(n)) = (a(n) + 2*b(n))/(a(n) + b(n))
    # So a(n+1) = a(n) + 2*b(n) and b(n+1) = a(n) + b(n)
    count = 0
    a, b = 1, 1
    for _ in range(1000):
        a, b = a + 2 * b, a + b
        if len(str(a)) > len(str(b)):
            count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=57)