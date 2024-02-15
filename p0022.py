from pathlib import Path


names = Path("data/p0022.txt").read_text()
names = names.strip('"').split('","')
names = sorted(names)
print(
    sum(
        sum(ord(c) - ord("A") + 1 for c in name) * (name_idx + 1)
        for name_idx, name in enumerate(names)
    )
)
