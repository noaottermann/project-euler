from euler import run
from utils import *

# Euler Problem 42

def solve():
    words = [word.strip('"') for word in open('p042_words.txt').read().split(',')]  
    total = 0
    for word in words:
        word_value = sum(ord(c) - ord('A') + 1 for c in word)
        if is_triangular(word_value):
            total += 1
    return total

if __name__ == '__main__':
    run(solve, problem_id=42)