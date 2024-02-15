def f(n: int):
    divisor_sums = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i * 2, n, i):
            divisor_sums[j] += i

    amicable_sum = 0
    for i, divisor_sum in enumerate(divisor_sums):
        if i == divisor_sum:
            continue
        if divisor_sum >= n:
            continue
        if divisor_sums[divisor_sum] != i:
            continue
        amicable_sum += i
    return amicable_sum


print(f(10_000))
