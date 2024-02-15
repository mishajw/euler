import math


def f(n: int):
    return math.factorial(n * 2) // (math.factorial(n) * math.factorial(n))


print(f(20))
