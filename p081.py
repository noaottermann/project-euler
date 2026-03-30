from euler import run
from utils import *

# Euler Problem 81

def solve():
    grid = [list(map(int, line.strip().split(','))) for line in open('p081_matrix.txt')]
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        dp[0][i] = dp[0][i-1] + grid[0][i]
    
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[-1][-1]

if __name__ == '__main__':
    run(solve, problem_id=81)