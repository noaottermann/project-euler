from euler import run
from utils import *

# Euler Problem 49

def solve():
    primes = [n for n in range(1000, 10000) if is_prime(n)]
    
    prime_groups = {}
    for prime in primes:
        key = ''.join(sorted(str(prime)))
        if key == "1478": # This is the known sequence, we want to skip it
            continue
        if key not in prime_groups:
            prime_groups[key] = []
        prime_groups[key].append(prime)
    
    for group in prime_groups.values():
        if len(group) < 3:
            continue
        group.sort()
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                c = b + (b - a)
                if c in group:
                    return str(a) + str(b) + str(c)

if __name__ == '__main__':
    run(solve, problem_id=49)