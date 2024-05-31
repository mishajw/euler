import math


def f(*, num_digits: int, n: int) -> int:
    digits = []
    for digit in range(num_digits):
        digit_value = n - 1
        digit_value %= math.factorial(num_digits - digit)
        digit_value //= math.factorial(num_digits - (digit + 1))
        digit_value = sorted(set(range(num_digits)) - set(digits))[digit_value]
        digits.append(digit_value)
    return int("".join(map(str, digits)))


print(f(num_digits=10, n=1_000_000))
