from euler import run
from math import isqrt

# Euler Problem 206

def solve():
    # We search n such that n^2 has the pattern 1_2_3_4_5_6_7_8_9_0.
    # n must be a multiple of 10 because the square ends with 0.
    # This means that n^2 will end with 900, so n must end with 30 or 70.
    # 1020304050607080900 <= n^2 <= 1929394959697989990
    low = isqrt(1020304050607080900)
    high = isqrt(1929394959697989990)
    start = low - (low % 100) + 30
    for n in range(start, high + 1, 100):
        square = n * n
        if is_concealed_square(square):
            return n
        n2 = n + 40
        if n2 <= high:
            square = n2 * n2
            if is_concealed_square(square):
                return n2

def is_concealed_square(square):
    s = str(square)
    return (
        len(s) == 19
        and s[0] == "1"
        and s[2] == "2"
        and s[4] == "3"
        and s[6] == "4"
        and s[8] == "5"
        and s[10] == "6"
        and s[12] == "7"
        and s[14] == "8"
        and s[16] == "9"
        and s[18] == "0"
    )

if __name__ == '__main__':
    run(solve, problem_id=206)