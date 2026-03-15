from euler import run
from utils import *
from datetime import datetime

# Euler Problem 19

def solve():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime(year, month, 1).weekday() == 6:
                count += 1
    return count

if __name__ == '__main__':
    run(solve, problem_id=19)