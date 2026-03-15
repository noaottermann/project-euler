from euler import run
from utils import *

# Euler Problem 15

def solve():
    # The number of paths from the top-left to the bottom-right of a n x n grid is given by the binomial coefficient C(2n, n) = (2n)! / (n! * n!)
    # Proof: To reach the bottom-right corner, you need to make n moves down and n moves right, in any order. The total number of moves is 2n, and you need to choose n of them to be down (or right). Hence, the formula C(2n, n).
    return nCr(40, 20)

if __name__ == '__main__':
    run(solve, problem_id=15)