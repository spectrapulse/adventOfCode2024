lines: list[str] = []

with open("input.txt", "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

midpoint = lines.index("")
first_half, second_half = lines[:midpoint], lines[midpoint + 1 :]


def map_first_part(s: str) -> tuple[int, int]:
    a, b = s.split("|")
    return int(a), int(b)


def map_second_part(s: str) -> list[int]:
    a = s.split(",")
    return list(map(int, a))


def is_entry_ok(a: int, l: list[int], orders: list[tuple[int, int]]) -> int:
    if len(l) == 0:
        return 0
    for x, y in orders:
        if y != a:
            continue
        if x not in l:
            continue
        return x
    return 0


def is_ordered_correctly(
    l: list[int], orders: list[tuple[int, int]]
) -> tuple[list[int], bool]:
    f = l.copy()
    i = 0
    has_changed = False
    while i < len(f):
        cur = f[i]
        res = is_entry_ok(cur, f[i + 1 :], orders)
        if res != 0:
            idx = f.index(res)
            print(i, idx, res, f)
            f[i], f[idx] = f[idx], f[i]
            has_changed = True
            continue
        i += 1
    return f, has_changed


a: list[tuple[int, int]] = list(map(map_first_part, first_half))
b: list[list[int]] = list(map(map_second_part, second_half))

result = 0

for i in b:
    f = is_ordered_correctly(i, a)
    print(i)
    print(f)
    if not f[1]:
        continue
    result += f[0][int((len(i) - 1) / 2)]


print(result)
