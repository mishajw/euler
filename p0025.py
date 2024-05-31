from itertools import count


def f(num_digits: int) -> int:
    f1, f2 = 1, 1
    for i in count(3):
        f3 = f1 + f2
        f1, f2 = f2, f3
        if f3 > 10 ** (num_digits - 1):
            return i
    raise ValueError()


print(f(1000))
