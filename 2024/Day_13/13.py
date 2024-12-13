import re

total = 0

for block in open("13.in").read().split("\n\n"):
    ax, ay, bx, by, px, py =  map(int, re.findall(r"\d+", block))
    min_score = float("inf")
    for i in range(101):
        for j in range(101):
            if ax * i + bx * j == px and ay * i + by * j == py:
                score = i * 3 + j
                min_score = min(min_score, score)
    if min_score != float("inf"):
        total += min_score
print(f"Résultat partie 1: {total}")

total2 = 0

for block in open("13.in").read().split("\n\n"):
    ax, ay, bx, by, px, py =  map(int, re.findall(r"\d+", block))
    px += 10000000000000
    py += 10000000000000

    sa = (px * by - py * bx) / (ax * by - ay * bx)
    sb = (px - ax * sa) / bx

    if sa % 1 == sb % 1 == 0:
        total2 += int(sa * 3 + sb)

print(f"Résultat partie 2: {total2}")