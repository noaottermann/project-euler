from euler import run
from utils import *

# Euler Problem 59

def solve():
    # Bruteforcing all 26^3 possibilities
    with open('p059_cipher.txt') as f:
        cipher = list(map(int, f.read().split(',')))
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key = [a, b, c]
                decrypted = [cipher[i] ^ key[i % 3] for i in range(len(cipher))]
                decrypted_text = ''.join(map(chr, decrypted))
                if [word in decrypted_text for word in [' the ', ' and ', ' to ', ' of ', ' a ', ' in ', ' that ', ' is ', ' was ', ' he ']].count(True) >= 3:
                    print(f'Key: {key}, Decrypted text: {decrypted_text}')
                    return sum(decrypted)

if __name__ == '__main__':
    run(solve, problem_id=59)