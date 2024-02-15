def f(n: int) -> int:
    return g(n, 3) + g(n, 5) - g(n, 3 * 5)


def g(n: int, multiple: int) -> int:
    result = (n - 1) // multiple
    result = (result * (result + 1)) // 2
    result *= multiple
    return result


print(f(1000))
