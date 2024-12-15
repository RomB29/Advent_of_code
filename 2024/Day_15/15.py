filename      = "15.in"
robot_symbole = "@"
box           = "O"
wall          = "#"
void          = "."


with open(filename, 'r') as f:
    parts = f.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")

n = len(grid)

dir = {
    "<": [-1, 0],
    ">": [1, 0],
    "^": [0, -1],
    "v": [0, 1]
}

for i in range(n):
    for j in range(n):
        if grid[i][j] == robot_symbole:
            robot_position = [i, j]

def is_wall(grid, rp):
    return grid[rp[1]][rp[0]] == wall

def is_box(grid, rp):
    return grid[rp[1]][rp[0]] == box

def is_void(grid, rp):
    return grid[rp[1]][rp[0]] == void

def count_boxes(grid, check_pos, direction):
    count = 1
    y_pos = check_pos[1]
    x_pos = check_pos[0]

    while (grid[y_pos + direction[1]][x_pos + direction[0]] != void and grid[y_pos + direction[1]][x_pos + direction[0]] != wall):
        x_pos = x_pos + direction[0]
        y_pos = y_pos + direction[1]
        count += 1

    last_position_type = grid[y_pos + direction[1]][x_pos + direction[0]]

    return count, last_position_type

def move_boxes(grid, pos, nb_boxes, direction):
    x_pos = pos[1]
    y_pos = pos[0]

    for nb in range(1, nb_boxes + 1):
        grid[x_pos + nb * direction[1]][y_pos + nb * direction[0]] = box
    grid[x_pos][y_pos] = void
def check_move(x, y, rp):
    return [rp[1] + y, rp[0] + x]



def move_robot(x, y, rp):
    grid[rp[0] + y][rp[1] + x] = robot_symbole
    grid[rp[0]][rp[1]] = void
    return [rp[0] + y, rp[1] + x]

for step in steps:
    direction = dir[step]
    i, j = direction[0], direction[1]
    virtual_movement = check_move(j, i, robot_position)

    if is_wall(grid, virtual_movement):
        continue

    if is_box(grid, virtual_movement):
        nb_boxes, end_pos = count_boxes(grid, virtual_movement, direction)

        if end_pos == void:
            move_boxes(grid, virtual_movement, nb_boxes, direction)
            robot_position = move_robot(i, j, robot_position)
            continue
        if end_pos == wall:
            continue

    if is_void(grid, virtual_movement):
        robot_position = move_robot(i, j, robot_position)


part_1 = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == box:
            part_1.append(i * 100 + j)

print(f"Solution part 1 : {sum(part_1)}")