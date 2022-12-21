import re

pattern = re.compile(r"-?\d+")

Y = 2000000

known = set()

intervals = []

for line in open("15.in"):
    sx, sy, bx, by = map(int, pattern.findall(line))
    
    d = abs(sx - bx) + abs(sy - by)
    o = d - abs(sy - Y)

    if o < 0:
        continue

    lx = sx - o
    hx = sx + o
    
    intervals.append((lx, hx))
    
    if by == Y:
        known.add(bx)


intervals.sort()

min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

ans = 0
for x in range(min_x, max_x):

    for left, right in intervals:
        if left <= x <= right:
            ans += 1
            break


print(ans)