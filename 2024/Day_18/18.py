from collections import deque
import numpy as np

coords = [list(map(int, line.split(","))) for line in open("18.in")]

n = 70
bytes = 8

def compute_way(bytes):
    grid = [[0] * (n + 1) for _ in range(n + 1 )]
    for x, y in coords[:bytes]:
        grid[y][x] = 1


    q = deque([(0, 0, 0)]) # row, colum, distance
    seen = {(0, 0)}
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    d = 0
    end = False
    while q:
        r, c, d = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > n or nc > n:
                continue

            if grid[nr][nc] == 1:
                continue

            if (nr, nc) in seen:
                continue

            if nr == nc == n:
                end = True
                break

            # if grid[nr][nc] == 0:
            seen.add((nr, nc))
            q.append((nr, nc, d + 1))

        if end:
            break

    if nr != nc != n:
        return False
    else:
        return True


bytes = np.arange(1 , len(coords) + 1)
bool_mask = True
for by in bytes:
    bool = compute_way(by)
    if bool == False:
        print(f"Solution part 2: {coords[by - 1]}")
        break
