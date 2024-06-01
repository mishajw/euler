from itertools import count, takewhile


def get_primes(max_value: int) -> list[int]:
    is_prime = [True for _ in range(max_value)]
    for i in range(2, max_value // 2):
        for j in range(i * 2, max_value, i):
            is_prime[j] = False
    primes = [i for i, prime in zip(range(max_value), is_prime) if prime]
    return primes[2:]


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def get_num_consecutive(a: int, b: int) -> int:
    return len(
        list(
            takewhile(
                is_prime,
                (n**2 + a * n + b for n in count()),
            )
        )
    )


primes = get_primes(1000 * 2)
abs = [
    (a, b)
    for b in primes
    for a in [p - b - 1 for p in primes]
    if abs(a) < 1000 and abs(b) <= 1000
]
a, b = max(abs, key=lambda p: get_num_consecutive(p[0], p[1]))
print(a * b)
