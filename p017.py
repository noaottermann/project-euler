from euler import run
from utils import *

# Euler Problem 17

def solve():
    num_words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    def number_to_words(n):
        if n == 1000:
            return "one thousand"
        words = ""
        if n >= 100:
            words += num_words[n // 100] + " hundred"
            n %= 100
            if n > 0:
                words += " and "
        if n >= 20:
            words += num_words[(n // 10) * 10]
            n %= 10
            if n > 0:
                words += "-"
        if n > 0:
            words += num_words[n]
        return words
    
    total_letters = sum(len(number_to_words(i).replace(" ", "").replace("-", "")) for i in range(1, 1001))
    return total_letters

if __name__ == '__main__':
    run(solve, problem_id=17)