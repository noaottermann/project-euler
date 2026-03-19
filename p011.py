from euler import run
from utils import *

# Euler Problem 11

def solve():
    grid = [[int(x) for x in line.strip().split()] for line in open('p011_grid.txt')]
    max_product = 0
    for i in range(20):
        for j in range(20):
            if j + 3 < 20:
                max_product = max(max_product, grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3])
            if i + 3 < 20:
                max_product = max(max_product, grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j])
            if i + 3 < 20 and j + 3 < 20:
                max_product = max(max_product, grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3])
            if i + 3 < 20 and j - 3 >= 0:
                max_product = max(max_product, grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3])
    return max_product

if __name__ == '__main__':
    run(solve, problem_id=11)