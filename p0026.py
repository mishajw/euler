from itertools import count


def num_recurring(n: int) -> int:
    seen: list[tuple[int, int]] = []
    d, r = 0, 1
    for idx in count():
        d, r = (r * 10) // n, (r * 10) % n
        if r == 0:
            return 0
        if (d, r) in seen:
            return idx - seen.index((d, r))
        seen.append((d, r))
    raise ValueError()


print(max(range(1, 1001), key=num_recurring))
