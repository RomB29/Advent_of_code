from collections import deque


filename      = "15.in"
robot_symbole = "@"
box_pattern   = ["[", "]"]
wall          = "#"
void          = "."


with open(filename, 'r') as f:
    parts = f.read().strip().split("\n\n")
    old_grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")

n = len(old_grid)

new_grid = [[0 for _ in range(2 * n)] for _ in range(n)]

dir = {
    "<": [-1, 0],
    ">": [1, 0],
    "^": [0, -1],
    "v": [0, 1]
}


def find_connected_boxes_from_robot(test, start_y, start_x, direction):
    visited = set()
    connected_boxes = set()
    queue = deque([(start_y, start_x)])

    dx, dy = direction

    def is_valid(y, x):
        return 0 <= y < len(test) and 0 <= x < len(test[0]) and test[y][x] in box_pattern

    def explore_box(y, x, dy, dx):

        if test[y][x] == '[':
            if is_valid(y, x + 1) and test[y][x + 1] == ']':
                connected_boxes.add(tuple(sorted([(y, x), (y, x + 1)])))
                queue.append((y, x + 1))
        elif test[y][x] == ']':
            if is_valid(y, x - 1) and test[y][x - 1] == '[':
                connected_boxes.add(tuple(sorted([(y, x), (y, x - 1)])))
                queue.append((y, x - 1))

        # Explore the next direction
        if test[y + dy][x + dx] != "." and test[y + dy][x + dx] != "#":
            queue.append((y + dy, x + dx))

    explore_box(start_y, start_x, dy, dx)

    while queue:
        y, x = queue.popleft()

        if (y, x) in visited:
            continue

        visited.add((y, x))

        ny, nx = y + dy, x + dx
        if is_valid(ny, nx) and (ny, nx) not in visited:
            explore_box(ny, nx, dy, dx)

    return list(connected_boxes)
def compute_new_grid(new_grid, old_grid, n):
    new_grid[0] = [wall for _ in range(len(new_grid[0]))]
    new_grid[-1] = [wall for _ in range(len(new_grid[-1]))]
    for i in range(1, len(old_grid) - 1):
        for j in range(len(old_grid[0])):

            if old_grid[i][j] == wall:
                new_grid[i][2 * j]            = wall
                new_grid[i][2 * j + 1]        = wall
            if old_grid[i][j] == "O":
                new_grid[i][2* j]             = "["
                new_grid[i][2 * j + 1]        = "]"
            if old_grid[i][j] == void:
                new_grid[i][2 * j]            = void
                new_grid[i][2 * j + 1]        = void
            if old_grid[i][j] == robot_symbole:
                new_grid[i][2 * j]     = robot_symbole
                new_grid[i][2 * j + 1] = void
    return new_grid
new_grid = compute_new_grid(new_grid, old_grid, n)


for i in range(n):
    t=1
    for j in range(2 * n):
        if new_grid[i][j] == robot_symbole:
            robot_position = [i, j]

def is_wall(new_grid, rp):
    return new_grid[rp[1]][rp[0]] == wall

def is_box(new_grid, rp):
    return new_grid[rp[1]][rp[0]] in box_pattern

def is_void(new_grid, rp):
    return new_grid[rp[1]][rp[0]] == void

def is_movable(new_grid, connected_boxes, nb_boxes, direction):

    for b in range(nb_boxes):
        for box in connected_boxes[b]:
            y, x = box

            if new_grid[y][x] == "#":
                return False

            new_y, new_x = y + direction[1], x + direction[0]

            if new_grid[new_y][new_x] == "#":
                return False
    return True
def move_boxes(new_grid, connected_boxes, nb_boxes, direction):

    temp_boxes = []
    symbol_map = {}

    for b in range(nb_boxes):
        temp_box = []
        for (y, x) in connected_boxes[b]:
            symbol_map[(y, x)] = new_grid[y][x]
            new_y, new_x = y + direction[1], x + direction[0]
            temp_box.append(((new_y, new_x), symbol_map[(y, x)]))
            new_grid[y][x] = "."

        temp_boxes.append(temp_box)

    for b in range(nb_boxes):
        for (new_y, new_x), symbol in temp_boxes[b]:
            new_grid[new_y][new_x] = symbol
    return new_grid
def check_move(x, y, rp):
    return [rp[1] + y, rp[0] + x]



def move_robot(x, y, rp):
    new_grid[rp[0] + y][rp[1] + x] = robot_symbole
    new_grid[rp[0]][rp[1]] = void
    return [rp[0] + y, rp[1] + x]

for i_s, step in enumerate(steps):
    direction = dir[step]
    i, j = direction[0], direction[1]
    virtual_movement = check_move(j, i, robot_position)

    if is_wall(new_grid, virtual_movement):
        continue

    if is_box(new_grid, virtual_movement):
        connected_boxes = find_connected_boxes_from_robot(new_grid, robot_position[0], robot_position[1], direction)
        nb_boxes        = len(connected_boxes)
        if is_movable(new_grid, connected_boxes, nb_boxes, direction):
            move_boxes(new_grid, connected_boxes, nb_boxes, direction)
            robot_position = move_robot(i, j, robot_position)
            continue
    if is_void(new_grid, virtual_movement):
        robot_position = move_robot(i, j, robot_position)


part_2 = []
for i in range(n):
    for j in range(2 * n):
        if new_grid[i][j] in box_pattern[0]:
            part_2.append(i * 100 + j)

print(f"Solution part 2 : {sum(part_2)}")