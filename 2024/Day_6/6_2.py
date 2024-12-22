# read input
import numpy as np
from tqdm import tqdm
from copy import deepcopy

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
            i_guard, j_guard = row, col
            break
    if found:
        break

res = 0
data_matrix = np.zeros((w_grid, l_grid))

while col > 0 and col < w_grid and row > 0 and row < l_grid:
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
    data_matrix[row][col] = 1

def will_loop(oi, oj):
    local_data = deepcopy(data)

    if local_data[oi][oj] == "#":
        return 0

    local_data[oi][oj] = "#"
    i, j = i_guard, j_guard

    dir = 0
    seen = set()

    while True:
        if (i, j, dir) in seen:
            local_data[oi][oj] = "."
            return 1

        seen.add((i, j, dir))

        next_i = i + all_directions[dir][0]
        next_j = j + all_directions[dir][1]

        if not (next_j >= 0 and next_j < w_grid and next_i >= 0 and next_i < l_grid):
            local_data[oi][oj] = "."
            return 0

        if local_data[next_i][next_j] == "#":
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j
            local_data[i][j] = "0"


res = int(np.sum(data_matrix)) + 1
print(res)

all_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
indices = np.where(data_matrix == 1)
coordinates = list(zip(indices[0], indices[1]))

ans = 0
for oi, oj in tqdm(coordinates):
    # if oi == row and oj == col:
    #     continue
    loop = will_loop(oi, oj)
    ans += loop

print(ans)