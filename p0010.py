def f(n: int) -> int:
    is_prime = [True] * n
    sum_of_primes = 0
    for i in range(2, n):
        if not is_prime[i]:
            continue
        sum_of_primes += i
        for j in range(i * 2, n, i):
            is_prime[j] = False
    return sum_of_primes


print(f(2_000_000))
