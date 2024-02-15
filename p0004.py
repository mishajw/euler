def f(n: int) -> int:
    values = sorted(
        [
            x * y
            for x in range(10 ** (n - 1), 10**n)
            for y in range(10 ** (n - 1), 10**n)
        ],
        reverse=True,
    )
    return next(filter(is_palindrome, values))


def is_palindrome(n: int) -> bool:
    s = str(n)
    return all(
        a == b
        for a, b in zip(
            s[: len(s) // 2 + 1],
            s[: len(s) // 2 - 1 : -1],
        )
    )


print(f(3))
