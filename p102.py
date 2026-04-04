from euler import run
from utils import *

# Euler Problem 102

def solve():
    count = 0
    with open("p102_triangles.txt", "r") as f:
        for line in f:
            x1, y1, x2, y2, x3, y3 = map(int, line.strip().split(","))
            area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
            if area > 0:
                area1 = abs(0*(y2-y3) + x2*(y3-0) + x3*(0-y2)) / 2
                area2 = abs(x1*(0-y3) + 0*(y3-y1) + x3*(y1-0)) / 2
                area3 = abs(x1*(y2-0) + x2*(0-y1) + 0*(y1-y2)) / 2
                if area == area1 + area2 + area3:
                    count += 1
    return count


if __name__ == '__main__':
    run(solve, problem_id=102)