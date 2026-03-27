from euler import run
from utils import *

# Euler Problem 61

def solve():
    prefixes = {}
    for s in range(3, 9):
        prefixes[s] = {}
        n = 1
        while True:
            p = polygonal(s, n)
            if p >= 10000:
                break
            if p >= 1000:
                prefix = p // 100
                prefixes[s].setdefault(prefix, []).append(p)
            n += 1

    used = set()
    used_types = set()
    for s in range(3, 9):
        for prefix, numbers in prefixes[s].items():
            for n in numbers:
                used.add(n)
                used_types.add(s)
                result = search(prefixes, n, used, used_types, prefix)
                if result is not None:
                    return sum(result)
                used.remove(n)
                used_types.remove(s)

def search(prefixes, n, used, used_types, first_prefix):
    if len(used) == 6:
        return [n] if n % 100 == first_prefix else None

    prefix = n % 100
    for next_s in range(3, 9):
        if next_s in used_types:
            continue
        for next_n in prefixes[next_s].get(prefix, []):
            if next_n not in used:
                used.add(next_n)
                used_types.add(next_s)
                result = search(prefixes, next_n, used, used_types, first_prefix)
                if result is not None:
                    return [n] + result
                used.remove(next_n)
                used_types.remove(next_s)
    
    
if __name__ == '__main__':
    run(solve, problem_id=61)