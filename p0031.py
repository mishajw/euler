def num_ways(n: int, ps: list[int]):
    if n == 0:
        return 1
    return sum(num_ways(n - p, ps[i:]) for i, p in enumerate(ps) if p <= n)


print(num_ways(200, ps=[200, 100, 50, 20, 10, 5, 2, 1]))
