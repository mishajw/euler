MAX = 1_000_000


def f(n: int) -> int:
    is_prime = [True] * MAX
    num_primes = 0
    for i in range(2, MAX):
        if not is_prime[i]:
            continue
        num_primes += 1
        if num_primes == n:
            return i
        for j in range(i * 2, MAX, i):
            is_prime[j] = False
    raise ValueError("MAX too low")


print(f(10_001))
