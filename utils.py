from functools import reduce
from itertools import permutations, product
from math import comb as _comb
from math import factorial as _factorial
from math import gcd as _gcd
from math import isqrt


_DIGIT_FACTORIALS = [
    1,
    1,
    2,
    6,
    24,
    120,
    720,
    5040,
    40320,
    362880,
]


def sum_digits(n):
    n = abs(n)
    total = 0
    while n:
        n, digit = divmod(n, 10)
        total += digit
    return total

def sum_squares_digits(n):
    n = abs(n)
    total = 0
    while n:
        n, digit = divmod(n, 10)
        total += digit * digit
    return total

def product_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    product = 1
    while n:
        n, digit = divmod(n, 10)
        product *= digit
    return product

def generate_permutations(*args):
    """
    Générateur de permutations intelligent s'adaptant au type d'entrée.
    Gère les chaînes, les listes, et les alternatives multiples.
    """
    if not args:
        return []

    if len(args) == 1 and isinstance(args[0], list):
        args = tuple(args[0])

    if len(args) == 1 and isinstance(args[0], str):
        s = args[0]
        if len(s) <= 1:
            return [s]
        return [''.join(p) for p in permutations(s)]

    normalized_args = []
    for arg in args:
        if isinstance(arg, list):
            normalized_args.append([str(item) for item in arg])
        else:
            normalized_args.append([str(arg)])

    final_permutations = []
    for combo in product(*normalized_args):
        for perm in permutations(combo):
            final_permutations.append(''.join(perm))

    return final_permutations

def proper_divisors(n):
    if n <= 1:
        return [1]
    divisors = [1]
    limit = isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            divisors.append(i)
            other = n // i
            if other != i:
                divisors.append(other)
    return divisors


def _sum_proper_divisors(n):
    if n <= 1:
        return 1
    total = 1
    limit = isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
    return total


def _all_divisors(n):
    if n <= 1:
        return [1]
    divisors = [1]
    temp = n
    exponent = 0
    while temp % 2 == 0:
        exponent += 1
        temp //= 2
    if exponent:
        current = divisors[:]
        mult = 1
        for _ in range(exponent):
            mult *= 2
            for d in current:
                divisors.append(d * mult)
    p = 3
    while p * p <= temp:
        exponent = 0
        while temp % p == 0:
            exponent += 1
            temp //= p
        if exponent:
            current = divisors[:]
            mult = 1
            for _ in range(exponent):
                mult *= p
                for d in current:
                    divisors.append(d * mult)
        p += 2
    if temp > 1:
        divisors += [d * temp for d in divisors]
    return divisors

def sum_of_divisors(n):
    if n <= 0:
        return n + 1
    if n == 1:
        return 2
    total = n + 1
    limit = isqrt(n)
    for i in range(2, limit + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
    return total

def is_abundant(n):
    return _sum_proper_divisors(n) > n

def is_deficient(n):
    return _sum_proper_divisors(n) < n

def is_perfect(n):
    return _sum_proper_divisors(n) == n

def are_amicable(a, b):
    return _sum_proper_divisors(a) == b and _sum_proper_divisors(b) == a

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors

def gcd(*args):
    return reduce(_gcd, args)
    
def lcm(*args):
    if not args:
        return 1

    def _lcm(a, b):
        return a // _gcd(a, b) * b

    return reduce(_lcm, args, 1)

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def factorial(n):
    return _factorial(n)

def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if bit == '0':
            a, b = c, d
        else:
            a, b = d, c + d
    return a
    
def is_perfect_square(n):
    if n < 0:
        return False
    root = isqrt(n)
    return root * root == n

def is_perfect_cube(n):
    if n < 0:
        root = round((-n) ** (1 / 3))
        return -root * root * root == n
    root = round(n ** (1 / 3))
    return root * root * root == n

def is_triangular(n):
    if n < 0:
        return False
    disc = 1 + 8 * n
    root = isqrt(disc)
    if root * root != disc:
        return False
    x = (root - 1) // 2
    return x * (x + 1) // 2 == n

def is_hexagonal(n):
    if n < 0:
        return False
    disc = 1 + 8 * n
    root = isqrt(disc)
    if root * root != disc:
        return False
    x = (1 + root) // 4
    return x * (2 * x - 1) == n

def is_pentagonal(n):
    if n < 0:
        return False
    disc = 1 + 24 * n
    root = isqrt(disc)
    if root * root != disc:
        return False
    x = (1 + root) // 6
    return x * (3 * x - 1) // 2 == n

def is_heptagonal(n):
    if n < 0:
        return False
    disc = 1 + 40 * n
    root = isqrt(disc)
    if root * root != disc:
        return False
    x = (1 + root) // 10
    return x * (5 * x - 3) // 2 == n

def is_octagonal(n):
    if n < 0:
        return False
    disc = 1 + 3 * n
    root = isqrt(disc)
    if root * root != disc:
        return False
    x = (1 + root) // 3
    return x * (3 * x - 2) == n

def is_sphenic(n):
    factors = prime_factors(n)
    return len(factors) == 3 and len(set(factors)) == 3

def is_square_free(n):
    factors = prime_factors(n)
    return len(set(factors)) == len(factors)

def is_coprime(a, b):
    return gcd(a, b) == 1

def is_perfect_power(n):
    if n <= 1:
        return False
    limit = isqrt(n)
    for base in range(2, limit + 1):
        result = base * base
        while result < n:
            result *= base
        if result == n:
            return True
    return False

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_multiple(a, b):
    return a % b == 0

def is_factor(a, b):
    return b % a == 0

def is_curious(n):
    return n == sum(_DIGIT_FACTORIALS[int(digit)] for digit in str(n))

def is_almost_prime(n, k):
    return len(set(prime_factors(n))) == k

def is_smooth(n, k):
    return all(factor <= k for factor in prime_factors(n))

def is_semi_prime(n):
    factors = prime_factors(n)
    return len(factors) == 2 and factors[0] != factors[1]

def is_pronic(n):
    if n < 0:
        return False
    root = isqrt(1 + 8 * n)
    x = (root - 1) // 2
    return x * (x + 1) == n

def is_kaprekar(n):
    if n == 1:
        return True
    sq = n ** 2
    str_sq = str(sq)
    for i in range(1, len(str_sq)):
        left = int(str_sq[:-i]) if str_sq[:-i] else 0
        right = int(str_sq[-i:]) if str_sq[-i:] else 0
        if left + right == n:
            return True
    return False

def is_narcissistic(n):
    digits = str(n)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == n

def is_rough(n, k):
    return all(factor >= k for factor in prime_factors(n))

def are_coprime(*args):
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            if _gcd(args[i], args[j]) != 1:
                return False
    return True

def is_smith(n):
    if n < 10:
        return False
    sum_d = sum_digits(n)
    sum_prime_factors = sum(sum_digits(factor) for factor in prime_factors(n))
    return sum_d == sum_prime_factors

def are_friendly(*args):
    if len(args) < 2:
        return False
    abundances = [_sum_proper_divisors(n) / n for n in args]
    return all(abundance == abundances[0] for abundance in abundances)

def is_harshad(n):
    sum_d = sum_digits(n)
    return n % sum_d == 0

def is_practical(n):
    if n < 2:
        return False
    divisors = _all_divisors(n)
    divisors.sort()
    reach = 0
    for d in divisors:
        if d > reach + 1:
            return False
        reach += d
        if reach >= n:
            return True
    return reach >= n

def is_automorphic(n):
    sq = n ** 2
    return str(sq).endswith(str(n))

def is_untouchable(n):
    if n < 2:
        return False
    for i in range(1, n):
        if _sum_proper_divisors(i) == n:
            return False
    return True

def reverse_num(num):
    rev = 0
    while num > 0:
        num, digit = divmod(num, 10)
        rev = rev * 10 + digit
    return rev

def is_emirp(n):
    if not is_prime(n):
        return False
    reversed_n = reverse_num(n)
    return n != reversed_n and is_prime(reversed_n)

def is_truncatable_prime(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
            return False
    return True

def is_truncatable_left(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def is_truncatable_right(n):
    if n < 10:
        return False
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[:len(str_n)-i])):
            return False
    return True

def are_permutations(*args):
    sorted_args = [sorted(str(arg)) for arg in args]
    return all(sorted_arg == sorted_args[0] for sorted_arg in sorted_args)

def is_pandigital(n, digits=None):
    str_n = str(n)
    if digits is None:
        digits = set(str(i) for i in range(1, len(str_n) + 1))
    else:
        digits = set(str(digit) for digit in digits)
    return set(str_n) == digits and len(str_n) == len(digits)

def sieve_of_eratosthenes(start, end=None):
    if end is None:
        start, end = 0, start
    if end <= 2:
        return [i for i in range(start, end) if i == 2]
    sieve = bytearray(b"\x01") * end
    sieve[0:2] = b"\x00\x00"
    limit = isqrt(end - 1)
    for i in range(2, limit + 1):
        if sieve[i]:
            start_i = i * i
            step = i
            sieve[start_i:end:step] = b"\x00" * (((end - start_i - 1) // step) + 1)
    return [i for i in range(start, end) if sieve[i]]

def count_divisors(n):
    count = 1
    temp = n
    exponent = 0
    while temp % 2 == 0:
        exponent += 1
        temp //= 2
    if exponent:
        count *= (exponent + 1)
    d = 3
    while d * d <= temp:
        exponent = 0
        while temp % d == 0:
            exponent += 1
            temp //= d
        if exponent:
            count *= (exponent + 1)
        d += 2
    if temp > 1:
        count *= 2
    return count

def collatz_length(n):
    length = 1
    while n != 1:
        if n & 1:
            n = 3 * n + 1
        else:
            n //= 2
        length += 1
    return length

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n & 1:
            n = 3 * n + 1
        else:
            n //= 2
        sequence.append(n)
    return sequence

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return _comb(n, r)

def recurring_cycle_length(n):
    remainders = {}
    remainder = 1
    position = 0
    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % n
        position += 1
    return 0

def is_curious_fraction(numerator, denominator):
    if numerator % 10 == 0 and denominator % 10 == 0:
        return False
    str_num = str(numerator)
    str_den = str(denominator)
    common_digits = set(str_num) & set(str_den)
    for digit in common_digits:
        if digit == '0':
            continue
        new_num_str = str_num.replace(digit, '', 1)
        new_den_str = str_den.replace(digit, '', 1)
        if new_num_str == '' or new_den_str == '':
            continue
        new_num = int(new_num_str)
        new_den = int(new_den_str)
        if new_den != 0 and numerator * new_den == denominator * new_num:
            return True
    return False

def are_sexy_primes(a, b):
    return is_prime(a) and is_prime(b) and abs(a - b) == 6

def is_twin_prime(n):
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))

def is_cousin_prime(n):
    return is_prime(n) and (is_prime(n - 4) or is_prime(n + 4))

def is_sophie_germain_prime(n):
    return is_prime(n) and is_prime(2 * n + 1)

def is_safe_prime(n):
    return is_prime(n) and is_prime((n - 1) // 2)

def is_mersenne_prime(n):
    if n < 1:
        return False
    m = n + 1
    if m & (m - 1) != 0:
        return False
    return is_prime(n)

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def is_composite(n):
    return n > 1 and not is_prime(n)

def distinct_prime_factors(n):
    count = 0
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:
                n //= d
        d += 2
    if n > 1:
        count += 1
    return count

def is_permutation(a, b):
    str_a = str(a)
    str_b = str(b)
    if len(str_a) != len(str_b):
        return False
    return sorted(str_a) == sorted(str_b)

def is_circular(n):
    str_n = str(n)
    for i in range(len(str_n)):
        rotated = int(str_n[i:] + str_n[:i])
        if rotated == n:
            return True
    return False

def is_circular_prime(n):
    if n < 10:
        return is_prime(n)
    str_n = str(n)
    for i in range(len(str_n)):
        rotated = int(str_n[i:] + str_n[:i])
        if not is_prime(rotated):
            return False
    return True

def is_circular_composite(n):
    if n < 10:
        return not is_prime(n) and n > 1
    str_n = str(n)
    for i in range(len(str_n)):
        rotated = int(str_n[i:] + str_n[:i])
        if is_prime(rotated) or rotated <= 1:
            return False
    return True

def is_circular_permutation(a, b):
    str_a = str(a)
    str_b = str(b)
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        rotated = str_a[i:] + str_a[:i]
        if rotated == str_b:
            return True
    return False

def is_lychrel(n, max_iterations=50):
    seen = set()
    while n not in seen and max_iterations > 0:
        seen.add(n)
        n += reverse_num(n)
        max_iterations -= 1
        if str(n) == str(n)[::-1]:
            return False
    return True

def is_happy(n, max_iterations=1000):
    seen = set()
    while n not in seen and max_iterations > 0:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
        max_iterations -= 1
        if n == 1:
            return True
    return False

def is_sad(n):
    return not is_happy(n)

def are_concat_primes(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

def polygonal(s, n):
    return n * (n * (s - 2) - (s - 4)) // 2
    
def are_cyclic(length=1, *args):
    if len(args) < 2:
        return False
    for i in range(len(args)):
        current = str(args[i])
        next_num = str(args[(i + 1) % len(args)])
        if current[-length:] != next_num[:length]:
            return False
    return True

def period_root_continued_fraction(n):
    if is_perfect_square(n):
        return []
    m = 0
    d = 1
    a0 = a = int(n**0.5)
    period = []
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)
        if a == 2 * a0:
            break
    return period

def to_digits(n):
    return list(map(int, str(n)))

def from_digits(digits):
    return int(''.join(map(str, digits)))

def add_to_digit_list(digits, number):
    carry = number
    for i in range(len(digits) - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10
        carry = total // 10
    while carry > 0:
        digits.insert(0, carry % 10)
        carry //= 10

def is_subsequence(sub, seq):
    it = iter(seq)
    return all(any(x == s for x in it) for s in sub)