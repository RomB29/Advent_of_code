from collections import defaultdict, deque


data = [line.strip() for line in open("12.in")]
n = len(data)


seeds = defaultdict()

for i in range(n):
    for j in range(n):
        if data[i][j] not in seeds:
            seeds[data[i][j]] = [(i, j)]
        else:
            seeds[data[i][j]].append((i, j))

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def is_valid(i, j):
    return 0 <= i < n and 0 <= j < n


def is_contour(group, i, j):
    for di, dj in dir:
        ni, nj = i + di, j + dj

        if not is_valid(ni, nj):
            return True

        if data[ni][nj] not in group:
            return True
    return False

def perimeter_counter(group, i, j):
    perimeter = 0
    for di, dj in dir:
        ni, nj = i + di, j + dj

        if not is_valid(ni, nj):
            perimeter += 1
            continue

        if data[ni][nj] not in group:
            perimeter += 1
            continue
    return perimeter


res = 0
temp = {}
for group in seeds:
    perimeter = 0
    flag = 1
    for i_s, (i_seed, j_seed) in enumerate(seeds[group]):
        visited = set()
        queue = deque([(i_seed, j_seed)])
        while queue:
            cur_i, cur_j = queue.popleft()
            visited.add((cur_i, cur_j))

            for n_i, n_j in dir:
                poss_i, poss_j = cur_i + n_i, cur_j + n_j

                if not is_valid(poss_i, poss_j):
                    continue

                if (poss_i, poss_j) in visited:
                    continue

                if data[poss_i][poss_j] == group:
                    queue.append((poss_i, poss_j))
                    visited.add((poss_i, poss_j))


        temp[group + str(i_s)] = visited

def sides(group):
    edges = {}
    for i, j in group:
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (ni, nj) in group:
                continue
            ei = (i + ni) / 2
            ej = (j + nj) / 2
            edges[(ei, ej)] = (ei - i, ej - j)

    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen:
            continue
        seen.add(edge)
        side_count += 1
        ei, ej = edge
        if ei % 1 == 0:
            for di in [-1, 1]:
                ci = ei + di
                while edges.get((ci, ej)) == direction:
                    seen.add((ci, ej))
                    ci += di
        else:
            for dj in [-1, 1]:
                cj = ej + dj
                while edges.get((ei, cj)) == direction:
                    seen.add((ei, cj))
                    cj += dj
    return side_count

group_by_coordinates = defaultdict(list)
for group, coordinates in temp.items():
    coordinate_set = frozenset(coordinates)
    group_by_coordinates[coordinate_set].append(group)

res = 0
for coordinate_set, groups in group_by_coordinates.items():
    print("*" * 80)
    print(groups[0][0])
    res += sides(coordinate_set) * len(coordinate_set)

print(res)