# read input
import numpy as np
from tqdm import tqdm

with open('6.in', 'r') as f:
    data = [list(line) for line in f.read().strip().split("\n")]

w_grid = len(data[0])
l_grid = len(data)
guard = "^"
found = 0
for row in range(w_grid):
    for col in range(l_grid):
        if data[row][col] == guard:
            found = True
            break
    if found:
        break

res = 0
data_matrix = np.zeros((w_grid, l_grid))

while col > 0 and col < w_grid - 1 and row > 0 and row < l_grid - 1:
    data_matrix[row][col] = "1"

    if guard == "^":
        row -= 1
        if data[row][col] == "#":
            guard = ">"
            row += 1

    if guard == ">":
        col += 1
        if data[row][col] == "#":
            guard = "v"
            col -= 1

    if guard == "v":
        row += 1
        if data[row][col] == "#":
            guard = "<"
            row -= 1

    if guard == "<":
        col -= 1
        if data[row][col] == "#":
            guard = "^"
            col += 1
def will_loop(oi, oj):
    if data[oi][oj] == "#":
        return False

    data[oi][oj] = "#"
    i, j = row, col

    dir = 0
    seen = set()
    while True:
        if (i, j, dir) in seen:
            data[oi][oj] = "."
            return True
        seen.add((i, j, dir))

        next_i = i + data[dir][0]
        next_j = j + data[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < n):
            data[oi][oj] = "."
            return False

        if data[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

res = int(np.sum(data_matrix))


indices = np.where(data_matrix == 1)
coordinates = list(zip(indices[0], indices[1]))
dsf = (9,7)
coordinates.append(dsf)
ans = 0
for oi, oj in tqdm(coordinates):
    loop = will_loop(oi, oj)
    ans += loop