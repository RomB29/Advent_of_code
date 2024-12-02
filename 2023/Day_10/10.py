import copy

class PipeSolver:
    """Class to calculate the closed loop of a pipe system"""

    def __init__(self, input_string):
        #             North     East    South   West
        self.moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.types = {
        #              N  E  S  W               N  E  S  W
        '-': {'goto': (0, 1, 0, 1), 'receive': (0, 1, 0, 1)}, # EAST_WEST
        '|': {'goto': (1, 0, 1, 0), 'receive': (1, 0, 1, 0)}, # NORTH_SOUTH
        'J': {'goto': (1, 0, 0, 1), 'receive': (0, 1, 1, 0)}, # NORTH_WEST
        'L': {'goto': (1, 1, 0, 0), 'receive': (0, 0, 1, 1)}, # NORTH_EAST
        'F': {'goto': (0, 1, 1, 0), 'receive': (1, 0, 0, 1)}, # SOUTH_EAST
        '7': {'goto': (0, 0, 1, 1), 'receive': (1, 1, 0, 0)}, # SOUTH_WEST
        }
        self.maze_lines = [list(line.strip()) for line in input_string.strip().split('\n')]
        self.maze_width = len(self.maze_lines[0])
        self.maze_height = len(self.maze_lines)
        self.start = 'S'
        self.ground = '.'
        self.start_location = (0,0)
        for i,maze in enumerate(self.maze_lines):
            for j,char in enumerate(maze):
                if char == self.start:
                    self.start_location = (i,j)

    def find_loop(self):
        # Try to solve maze with BFS like algorithm
        for key,_ in self.types.items():
            tmp_maze = [copy.deepcopy(line) for line in self.maze_lines]
            path = [self.start_location]
            tmp_maze[self.start_location[0]][self.start_location[1]] = key
            cur_location = self.start_location
            cur_type = key
            while True:
                for i, move in enumerate(self.moves):
                    new_location = (cur_location[0] + move[0], cur_location[1] + move[1]) # Set the move we will take and what the location will be
                    if (
                        0 <= new_location[0] < self.maze_height    # Check bounds for Y coordinate
                        and 0 <= new_location[1] < self.maze_width # Check bounds for X coordinate
                        and tmp_maze[new_location[0]][new_location[1]] != self.ground # Make sure not == ground
                        and tmp_maze[new_location[0]][new_location[1]] != cur_location # Make sure not == cur_location
                        and (
                            self.types[cur_type]['goto'][i] == 1
                            and self.types[tmp_maze[new_location[0]][new_location[1]]]['receive'][i] == 1
                        ) # Confirm we can go to the spot and the next spot can receive it
                    ):
                        if new_location == self.start_location and len(path) > 2: # See if our new_location is the same as our start
                            return len(path) // 2, path, tmp_maze

                        elif (cur_location[0] + move[0], cur_location[1] + move[1]) not in path: # Make sure we haven't visited location:
                            cur_location = (cur_location[0] + move[0], cur_location[1] + move[1])
                            cur_type = tmp_maze[cur_location[0]][cur_location[1]]
                            path.append(cur_location)
                            break
                else:
                    if cur_location != self.start_location:
                        tmp_maze[cur_location[0]][cur_location[1]] = self.ground
                    if not path:
                        break
                    path.pop()
                    if path:
                        cur_location = path[-1]
                        cur_type = tmp_maze[cur_location[0]][cur_location[1]]


    def ray_cast(self, closed_loop, tmp_maze):
        grid = [[self.ground if (row, column) not in closed_loop else tmp_maze[row][column]
                for column in range(self.maze_width)] for row in range(self.maze_height)]

        for line in grid: print(''.join(line))

        # RAY CASTING ALGORITHM
        interior = 0
        for row in grid:
            for i, char in enumerate(row):
                if char != self.ground:
                    continue

                intersect = 0
                corner_pipes = []
                for j in range(i, len(row)):
                    if row[j] == "|":
                        intersect += 1
                    if row[j] in "FL":
                        corner_pipes.append(row[j])
                    if (
                        len(corner_pipes) != 0
                        and row[j] == "J"
                        and corner_pipes[-1] == "F"
                        or row[j] == "7" and corner_pipes[-1] == "L"
                        ):
                        corner_pipes.pop(-1)
                        intersect += 1

                if intersect % 2 == 1:
                    interior += 1

        return interior

    def part_1(self):
        result, _, tmp_maze = self.find_loop()
        #for line in tmp_maze: print(''.join(line))
        return result

    def part_2(self):
        _, path, tmp_maze = self.find_loop()
        interior = self.ray_cast(path, tmp_maze)
        return interior

if __name__ == "__main__":
    # input_string = """
    # .F----7F7F7F7F-7....
    # .|F--7||||||||FJ....
    # .||.FJ||||||||L7....
    # FJL7L7LJLJ||LJ.L-7..
    # L--J.L7...LJS7F-7L7.
    # ....F-J..F7FJ|L7L7L7
    # ....L7.F7||L7|.L7L7|
    # .....|FJLJ|FJ|F7|.LJ
    # ....FJL-7.||.||||...
    # ....L---J.LJ.LJLJ...
    # """

    with open('10.in', 'r') as file:
        input_string = file.read()

    pipe_solver = PipeSolver(input_string)
    part_1_result = pipe_solver.part_1()
    part_2_result = pipe_solver.part_2()
    print(f'Part 1: {part_1_result}')
    print(f'Part 2: {part_2_result}')