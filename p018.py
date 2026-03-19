from euler import run
from utils import *

# Euler Problem 18

def solve():
    triangle = [list(map(int, line.strip().split())) for line in open('p018_triangle.txt')]

    for row in range(len(triangle) -2,-1,-1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])
    
    return triangle[0][0]

if __name__ == '__main__':
    run(solve, problem_id=18)