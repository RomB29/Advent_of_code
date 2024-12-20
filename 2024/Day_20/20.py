from tqdm import tqdm

grid = [list(line.strip()) for line in open("20.in")]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break
t=1

dists = [[-1] * cols for _ in range(rows)]
dists[r][c] = 0

while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            continue
        if grid[nr][nc] == "#":
            continue
        if dists[nr][nc] != -1:
            continue
        dists[nr][nc] = dists[r][c] + 1
        r = nr
        c = nc

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#":
            continue
        for nr, nc in [(r + 2, c), (r + 1, c + 1), (r, c + 2), (r - 2, c), (r - 1, c + 1), (r, c - 2), (r - 1, c - 1), (r + 1, c - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] == "#":
                continue
            if (dists[nr][nc] - dists[r][c]) >= 101:
                count += 1
print(count)

##part 2 :
count2 = 0
for r in tqdm(range(rows), desc="Processing rows"):
    for c in range(cols):
        if grid[r][c] == "#":
            continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r - dr, c + dc), (r + dr, c - dc), (r - dr, c - dc)}:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == "#":
                        continue
                    if (dists[nr][nc] - dists[r][c]) >= 100 + radius:
                        count2 += 1
print(count2)
