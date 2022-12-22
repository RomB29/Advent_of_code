import numpy as np
import re
file_path = "22.in"

with open(file_path) as f:
    datas = f.read().split("\n")

width = 0
for columns in datas[:-2]:
    width = max(width, len(columns))

matrix = [line + " " * (width - len(line)) for line in datas]


first_index = [i for i, val in enumerate(matrix[0]) if val == '.'][0]

x = 0
y = (first_index - 1)
facing = 0  # 0 = right, 1 = down, 2 = left, 3 = up

def check_up_down_boundaries(x=None, y=None):

    if y is not None and x is None:
        column = [row[y] for row in matrix[:-2]]
        boundaries = [pixel for pixel, y in enumerate(column) if y != ' ']

    if x is not None and y is None:
        column = [row for row in matrix[x]]
        boundaries = [pixel for pixel, x in enumerate(column) if x != ' ']   

    return boundaries[0], boundaries[-1]


    


input_instructions = matrix[-1]
instructions = re.findall(r'(\d+)([RL]?)', input_instructions)

for case, instr in instructions:
    move = int(case)

    while(move > 0):

        if facing == 0: # right
            if (y + 1 == width) or matrix[x][y + 1] == ' ':
                ymin, ymax = check_up_down_boundaries(x, None)
                y = ymin

                if matrix[x][y] == '#':
                    y = ymax
                    break
            else:
                y += 1
                

        if facing == 1: # bottom
            if (x + 1 == len(matrix[0:-2])) or matrix[x + 1][y] == ' ':
                xmin, xmax  = check_up_down_boundaries(None, y)
                x = xmin

                if matrix[x][y] == '#':
                    x = xmax
                    break

            else:
                x += 1


        if facing == 2: # left
            if (y - 1 < 0) or matrix[x][y - 1] == ' ':
                ymin, ymax = check_up_down_boundaries(x, None)
                y = ymax

                if matrix[x][y] == '#':
                    y = ymin
                    break
            # elif y - 1 < 0:
            #     y = (y - 1) % width
            else:
                y -= 1


        if facing == 3: # up
            if (x - 1 < 0) or matrix[x - 1][y] == ' ':
                xmin, xmax = check_up_down_boundaries(None, y)
                x = xmax

                if matrix[x][y] == '#':
                    x = xmin
                    break

            # elif (x - 1) < 0:
            #     x = (x - 1) % len(matrix[:-2])
            else:
                x -= 1


        if matrix[x][y] == "#":
            if facing == 0:
                y -= 1
            if facing == 1:
                x -= 1
            if facing == 2:
                y += 1
            if facing == 3:
                x += 1
            break

        move -= 1
        
    if instr == "R":
        facing = (facing + 1) % 4
    if instr == "L":
        facing = (facing - 1) % 4



print(f"Final password is: {1000 * (x + 1) + 4 * (y + 1) + facing}")
t=1