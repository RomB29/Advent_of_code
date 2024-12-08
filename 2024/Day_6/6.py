# read input
import numpy as np

with open('6.in', 'r') as f:
    data = f.read().split('\n')

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

res = int(np.sum(data_matrix))
print(f"Résultat partie 1: {res + 1}")
