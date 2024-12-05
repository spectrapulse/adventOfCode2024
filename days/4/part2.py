lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

WIDTH, HEIGHT = 140, 140

result = 0


def is_valid_x_mas(x: int, y: int) -> bool:
    if lines[y + 1][x + 1] != "A":
        return False
    a, b, c, d = lines[y][x], lines[y][x + 2], lines[y + 2][x], lines[y + 2][x + 2]
    if not (a == "M" and d == "S" or a == "S" and d == "M"):
        return False
    return b == "M" and c == "S" or b == "S" and c == "M"


for x in range(WIDTH - 2):
    for y in range(HEIGHT - 2):
        result += 1 if is_valid_x_mas(x, y) else 0

print(result)
