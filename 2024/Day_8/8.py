import numpy as np

with open("8.in", 'r') as f:
    data = f.read().splitlines()

rows     = len(data)
cols     = len(data[0])
antennas = {}
antinodes = set()


for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char != ".":
            if char in antennas:
                antennas[char].append((r, c))

            if char not in antennas:
                antennas[char] = []
                antennas[char].append((r, c))

def distance(xa, ya, xb, yb):
    return (xb - xa), (yb - ya)

for tup in antennas.values():
    for i, (x1, y1) in enumerate(tup):
        for j, (x2, y2) in enumerate(tup[i + 1:]):
            dr, dc = distance(x1, y1, x2, y2)

            r = x1
            c = y1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r += dr
                c += dc

            r2 = x2
            c2 = y2
            while 0 <= r2 < rows and 0 <= c2 < cols:
                antinodes.add((r2, c2))
                r2 -= dr
                c2 -= dc

possible_antinodes = [res for res in antinodes if 0 <= res[0] < rows and 0 <= res[1] < cols]

print(f"Solution part 1: {len(possible_antinodes)}")