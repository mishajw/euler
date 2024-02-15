def f(n: int) -> int:
    result = 2  # start with 2 for the initial `y` value.
    x, y = 1, 2
    while True:
        z = x + y
        if z % 2 == 0:
            result += z
        if z > n:
            break
        x, y = y, z
    return result


print(f(4_000_000))
