filename = "14.in"

with open(filename) as f:
    lines = f.read().strip().split("\n")

j = 101
i = 103
# j = 11
# i = 7

nb_seconds = 8300

matrix = [[0 for _ in range(j)] for _ in range(i)]

p = []
v = []

for line in lines:
    a, b = line.split(" ")
    p.append(tuple(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))


def update(p: list[tuple], v: list[tuple]):
    for index, (x, y) in enumerate(p):
        temp = list(p[index])
        temp[0] = (x + v[index][0]) % j
        temp[1] = (y + v[index][1]) % i
        p[index] = tuple(temp)

def count_robots(rx, ry, p):
    count = 0
    for index, (x, y) in enumerate(p):
        for x in rx:
            for y in ry:
                if p[index][0] == x and p[index][1] == y:
                    count += 1
    return count

def plot_robots(p, second, file):
    for n in range(i):
        for m in range(j):
            matrix[n][m] = " "
    for index, (x, y) in enumerate(p):
        matrix[y][x] = "#"

    matrix_str = "\n".join("".join(row) for row in matrix)
    print(f"{second}")
    print(matrix_str + "\n \n \n")
    # Écrire l'itération et la matrice dans le fichier
    file.write(f"second {second}\n")
    file.write(matrix_str + "\n\n\n")


t=0
with open(f"all_seconds_{t}.txt", "w") as file:
    for second in range(1, nb_seconds):
        update(p, v)
        if second >= 8000:
            plot_robots(p, second, file)


r1x = list(range(0, j // 2))
r1y = list(range(0, i // 2))

r2x = list(range(j // 2 + 1, j))
r2y = list(range(i // 2 + 1, i))

first_quadrant  = count_robots(r1x, r1y, p)

second_quadrant = count_robots(r2x, r1y, p)
third_quadrant  = count_robots(r1x, r2y, p)
fourth_quadrant = count_robots(r2x, r2y, p)

print(f"Solution part 1: {first_quadrant * second_quadrant * third_quadrant * fourth_quadrant}")