from itertools import count
from typing import Iterable

MAX = 1_000_000


def f(n: int) -> int:
    primes = list(get_primes())
    triangle_number = 0
    for i in count(1):
        triangle_number += i
        if get_prime_factors(triangle_number, primes) > n:
            return triangle_number
    raise ValueError()


def get_primes() -> Iterable[int]:
    is_prime = [True] * MAX
    for i in range(2, MAX):
        if not is_prime[i]:
            continue
        yield i
        for j in range(i * 2, MAX, i):
            is_prime[j] = False


def get_prime_factors(n: int, primes: list[int]) -> int:
    assert n > 0
    num_divisors = 1
    for prime in primes:
        if n == 1:
            break
        num_prime_divisors = 0
        while n % prime == 0:
            num_prime_divisors += 1
            n //= prime
        num_divisors *= num_prime_divisors + 1
    return num_divisors


print(f(500))
