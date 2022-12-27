filename = "9_part2.in"

with open(filename) as f:
    datas = f.read().strip().split("\n")

possible_movement = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

knot_positions = [[0, 0] for _ in range(10)]

def head_tail_separation(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def move(dx, dy):
    global knot_positions

    knot_positions[0][0] += dx # head x position
    knot_positions[0][1] += dy # head y position

    for i in range(1, 10):
        
        head_x, head_y = knot_positions[i - 1]
        tail_x, tail_y = knot_positions[i]

        if not head_tail_separation(head_x, head_y, tail_x, tail_y):
            """
            The expression (head_x - tail_x) / abs(head_x - tail_x) will return the following values:

            If head_x is equal to tail_x, the expression will return 0.
            If head_x is greater than tail_x, the expression will return 1.
            If head_x is less than tail_x, the expression will return -1.
            This expression can be used to determine the direction in which the tail needs to move in order to be adjacent to the head. For example, if the head 
            is to the right of the tail, the expression will return 1, indicating that the tail should move one step to the right in order to be adjacent to the head. Similarly, if the head is to the left of the tail, the expression will return -1, indicating that the tail should move one step to the left.

            It's worth noting that this expression only works if the head and tail are not already adjacent or touching. If they are already adjacent or touching, 
            the expression will return 0, which may not be the correct result. In that case, you may need to use a different approach to determine the direction in 
            which the tail needs to move.

            """

            new_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
            new_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)

            tail_x += new_x
            tail_y += new_y

        knot_positions[i] = [tail_x, tail_y]

tail_visited = set()
tail_visited.add(tuple(knot_positions[-1]))

for line in datas:
    movement, distance = line.split(" ")
    distance = int(distance)

    dx, dy = possible_movement[movement]
    for _ in range(distance):
        move(dx, dy)
        tail_visited.add(tuple(knot_positions[-1]))

print(f"Number of tail visited: {len(tail_visited)} ")