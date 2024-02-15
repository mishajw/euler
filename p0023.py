def f(n: int):
    divisor_sums = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i * 2, n, i):
            divisor_sums[j] += i
    abundant_numbers = [
        i for i, divisor_sum in enumerate(divisor_sums) if i < divisor_sum and i != 0
    ]
    is_summable = [False for _ in range(n)]
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j < n:
                is_summable[i + j] = True
    sum_of_summable = 0
    for i, is_sum in enumerate(is_summable):
        if not is_sum:
            sum_of_summable += i
    return sum_of_summable


print(f(28123))
