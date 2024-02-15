def f(n: int) -> int:
    largest = None
    for i in range(3, n // 2, 2):
        if n % i == 0:
            largest = i
            n //= i
        if n == 1:
            break
    assert largest is not None
    return largest


print(f(600851475143))
