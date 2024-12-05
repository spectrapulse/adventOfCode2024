import numpy as np

lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = np.array(list(map(list, lines)))

lines_t = lines.transpose()

diags = [lines[::-1, :].diagonal(i) for i in range(-lines.shape[0] + 1, lines.shape[1])]
diags.extend(lines.diagonal(i) for i in range(lines.shape[1] - 1, -lines.shape[0], -1))

lines = ["".join(n) for n in lines]
lines_t = ["".join(n) for n in lines_t]
diags = ["".join(n) for n in diags]

WIDTH, HEIGHT = 140, 140

result = 0

result += sum(map(lambda x: x.count("XMAS"), lines))
result += sum(map(lambda x: x.count("XMAS"), lines_t))
result += sum(map(lambda x: x.count("XMAS"), diags))
result += sum(map(lambda x: x.count("SAMX"), lines))
result += sum(map(lambda x: x.count("SAMX"), lines_t))
result += sum(map(lambda x: x.count("SAMX"), diags))

print(result)
