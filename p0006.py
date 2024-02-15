def f(n: int):
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    sum_of_square = sum(i**2 for i in range(1, n + 1))
    return square_of_sum - sum_of_square


print(f(100))
