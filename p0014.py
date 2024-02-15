def f(n: int) -> int:
    num_steps_by_input: dict[int, int] = dict()

    def record_steps(steps_left: int, steps: list[int]) -> None:
        for step_idx, step in enumerate(steps):
            assert step not in num_steps_by_input
            num_steps_by_input[step] = len(steps) - step_idx + steps_left

    def get_num_steps(n: int) -> int:
        steps = []
        while True:
            if n in num_steps_by_input:
                record_steps(num_steps_by_input[n], steps)
                return len(steps) + num_steps_by_input[n]
            steps.append(n)
            if n == 1:
                record_steps(0, steps)
                return len(steps) + num_steps_by_input[n]
            elif n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1

    return max(range(1, n), key=get_num_steps)


print(f(1_000_000))
