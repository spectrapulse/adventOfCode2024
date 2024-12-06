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


def is_entry_ok(a: int, l: list[int], orders: list[tuple[int, int]]) -> bool:
    if len(l) == 0:
        return True
    for x, y in orders:
        if y != a:
            continue
        if x not in l:
            continue
        return False
    return True


def is_ordered_correctly(l: list[int], orders: list[tuple[int, int]]) -> bool:
    for i in range(len(l)):
        cur = l[i]
        if not is_entry_ok(cur, l[i + 1 :], orders):
            return False
    return True


a: list[tuple[int, int]] = list(map(map_first_part, first_half))
b: list[list[int]] = list(map(map_second_part, second_half))

result = 0

for i in b:
    if is_ordered_correctly(i, a):
        result += i[int((len(i) - 1) / 2)]


print(result)
