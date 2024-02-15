from collections import defaultdict
from itertools import groupby
from typing import Iterable


def f(n: int) -> int:
    num_primes: dict[int, int] = defaultdict(int)
    for i in range(n + 1):
        for prime, group in groupby(find_prime_factors(i)):
            x = len(list(group))
            num_primes[prime] = max(num_primes[prime], x)
    result = 1
    for prime, num in num_primes.items():
        result *= prime**num
    return result


def find_prime_factors(n: int) -> Iterable[int]:
    i = 2
    while i <= n:
        if n % i == 0:
            yield i
            n //= i
        else:
            i += 1


print(f(20))
