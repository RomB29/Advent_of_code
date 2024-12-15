from collections import deque

def find_robot_position(test):
    # Trouver la position du robot dans la grille
    for y in range(len(test)):
        for x in range(len(test[0])):
            if test[y][x] == '@':
                return y, x
    return None

def find_connected_boxes_from_robot(test, start_y, start_x, direction):
    visited = set()
    connected_boxes = []
    queue = deque([(start_y, start_x)])

    dy, dx = direction

    def is_valid(y, x):
        return 0 <= y < len(test) and 0 <= x < len(test[0]) and test[y][x] in ['[', ']']

    def explore_box(y, x, dy, dx):

        if test[y][x] == '[':

            if is_valid(y, x + 1) and test[y][x + 1] == ']':
                connected_boxes.append([(y, x), (y, x + 1)])
                queue.append((y, x + 1))
        elif test[y][x] == ']':

            if is_valid(y, x - 1) and test[y][x - 1] == '[':
                connected_boxes.append([(y, x), (y, x - 1)])
                queue.append((y, x - 1))
        queue.append((y + dy, dx + dx))

    explore_box(start_y, start_x, dy, dx)


    while queue:
        y, x = queue.popleft()


        if (y, x) in visited:
            continue

        visited.add((y, x))


        ny, nx = y + dy, x + dx
        if is_valid(ny, nx) and (ny, nx) not in visited:
            explore_box(ny, nx, dy, dx)
            queue.append((ny, nx))

    return connected_boxes

# Test avec un exemple
test = [
    ["#", "#", "#", "#"],
    [".", ".", ".", "."],
    ["[", "]", "[", "]"],
    [".", "[", "]", "."],
    ["[", "]", "[", "]"],
    ["[", "]", "@", "#"]
]

# Trouver la position du robot (notée "@")
robot_pos = find_robot_position(test)
box = ["[", "]"]
if robot_pos:
    start_y, start_x = robot_pos
    # Direction verticale vers le haut : (dy = -1, dx = 0) (chercher vers le haut)
    direction = (0, -1)

    # Trouver les boîtes connectées à partir de la position du robot
    connected_boxes = find_connected_boxes_from_robot(test, start_y, start_x, direction)

    # Affichage des résultats
    print(f"Boîtes connectées dans la direction donnée à partir du robot : {connected_boxes}")
else:
    print("Le robot n'a pas été trouvé dans la grille.")
