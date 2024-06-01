import math


def f(n: int):
    num_digits = int(math.log(n, 10)) + 1
    digits = [(n // 10**i) % 10 for i in range(num_digits)]
    return sum(d**5 for d in digits)


assert (9**5 * 7) < 10**7
print(sum(n for n in range(2, 10**6) if n == f(n)))
