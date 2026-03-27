def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def product_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
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
        permutations = []
        for i, char in enumerate(s):
            for perm in generate_permutations(s[:i] + s[i+1:]):
                permutations.append(char + perm)
        return permutations
    else:
        normalized_args = []
        for arg in args:
            if isinstance(arg, list):
                normalized_args.append(arg)
            else:
                normalized_args.append([str(arg)])

        def get_combinations(lists):
            if not lists:
                return [[]]
            first_list = lists[0]
            rest_combinations = get_combinations(lists[1:])
            
            combos = []
            for item in first_list:
                for combo in rest_combinations:
                    combos.append([str(item)] + combo)
            return combos

        def _permute_items(items):
            if len(items) == 1:
                return [items[0]]
            perms = []
            for i, item in enumerate(items):
                for p in _permute_items(items[:i] + items[i+1:]):
                    perms.append(item + p)
            return perms

        all_combinations = get_combinations(normalized_args)
        
        final_permutations = []
        for combo in all_combinations:
            final_permutations.extend(_permute_items(combo))
            
        return final_permutations

def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def sum_of_divisors(n):
    total = n+1
    for i in range(2, n):
        if n % i == 0:
            total += i
    return total

def is_abundant(n):
    return sum(proper_divisors(n)) > n

def is_deficient(n):
    return sum(proper_divisors(n)) < n

def is_perfect(n):
    return sum(proper_divisors(n)) == n

def are_amicable(a, b):
    return sum(proper_divisors(a)) == b and sum(proper_divisors(b)) == a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def gcd(*args):
    gcd_value = args[0]
    for num in args[1:]:
        while num:
            gcd_value, num = num, gcd_value % num
    return gcd_value
    
def lcm(*args):
    lcm_value = 1
    for num in args:
        lcm_value = lcm_value * num // gcd(lcm_value, num)
    return lcm_value

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def is_perfect_square(n):
    return int(n**0.5)**2 == n

def is_perfect_cube(n):
    return int(n**(1/3))**3 == n

def is_triangular(n):
    x = (int(((-1 + (1 + 8 * n)**0.5) / 2)))
    return x * (x + 1) // 2 == n

def is_hexagonal(n):
    x = (int((1 + (1 + 8 * n)**0.5) / 4))
    return x * (2 * x - 1) == n

def is_pentagonal(n):
    x = (int((1 + (1 + 24 * n)**0.5) / 6))
    return x * (3 * x - 1) // 2 == n

def is_heptagonal(n):
    x = (int((1 + (1 + 40 * n)**0.5) / 10))
    return x * (5 * x - 3) // 2 == n

def is_octagonal(n):
    x = (int((1 + (1 + 3 * n)**0.5) / 3))
    return x * (3 * x - 2) == n

def is_sphenic(n):
    factors = set(prime_factors(n))
    return len(factors) == 3 and all(prime_factors(n).count(factor) == 1 for factor in factors)

def is_square_free(n):
    factors = prime_factors(n)
    return len(set(factors)) == len(factors)

def is_coprime(a, b):
    return gcd(a, b) == 1

def is_perfect_power(n):
    for base in range(2, int(n**0.5) + 1):
        power = 2
        while True:
            result = base ** power
            if result == n:
                return True
            elif result > n:
                break
            power += 1
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
    return n == sum(factorial(int(digit)) for digit in str(n))

def is_almost_prime(n, k):
    return len(set(prime_factors(n))) == k

def is_smooth(n, k):
    return all(factor <= k for factor in prime_factors(n))

def is_semi_prime(n):
    factors = prime_factors(n)
    return len(factors) == 2 and factors[0] != factors[1]

def is_pronic(n):
    x = int(((-1 + (1 + 8 * n)**0.5) / 2))
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
            if not is_coprime(args[i], args[j]):
                return False
    return True

def is_smith(n):
    if n < 10:
        return False
    sum_d = sum_digits(n)
    sum_prime_factors = sum(sum(int(digit) for digit in str(factor)) for factor in prime_factors(n))
    return sum_d == sum_prime_factors

def are_friendly(*args):
    if len(args) < 2:
        return False
    abundances = [sum(proper_divisors(n)) / n for n in args]
    return all(abundance == abundances[0] for abundance in abundances)

def is_harshad(n):
    sum_d = sum_digits(n)
    return n % sum_d == 0

def is_practical(n):
    if n < 2:
        return False
    divisors = proper_divisors(n)
    divisors.append(0)
    divisors.sort()
    can_make = [False] * (n + 1)
    can_make[0] = True
    for divisor in divisors:
        for i in range(n - divisor, -1, -1):
            if can_make[i]:
                can_make[i + divisor] = True
    return all(can_make[i] for i in range(1, n + 1))

def is_automorphic(n):
    sq = n ** 2
    return str(sq).endswith(str(n))

def is_untouchable(n):
    if n < 2:
        return False
    for i in range(1, n):
        if sum(proper_divisors(i)) == n:
            return False
    return True

def reverse_num(num):
        return int(str(num)[::-1])

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
    sieve = [True] * end
    sieve[0] = sieve[1] = False
    for i in range(2, int(end**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end, i):
                sieve[j] = False
    return [i for i in range(start, end) if sieve[i]]

def count_divisors(n):
    count = 1
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            exponent = 0
            while temp % d == 0:
                exponent += 1
                temp //= d
            count *= (exponent + 1)
        d += 1
    if temp > 1:
        count *= 2
    return count

def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
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
    if r == 0 or r == n:
        return 1
    # C(n, r) == C(n, n-r)
    r = min(r, n - r)  
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

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
    p = 1
    while True:
        mersenne = (1 << p) - 1  # 2^p - 1
        if mersenne == n:
            return is_prime(mersenne)
        elif mersenne > n:
            return False
        p += 1

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def is_composite(n):
    return n > 1 and not is_prime(n)

def distinct_prime_factors(n):
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
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

def period_continued_fraction(n):
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