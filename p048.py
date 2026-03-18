from euler import run
from utils import *

# Euler Problem 48

def solve():
    return str(sum(i**i for i in range(1, 1001)))[-10:]

if __name__ == '__main__':
    run(solve, problem_id=48)