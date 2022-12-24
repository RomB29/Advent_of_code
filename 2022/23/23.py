from collections import deque
import copy
# Constants representing the possible states of a tile
ELF = '#'
GROUND = '.'

directions = [(-1, 0, 'N'), (1, 0, 'S'), (0, -1, 'W'), (0, 1, 'E'), (-1, -1, 'NW'), (-1, 1, 'NE'), (1, -1, 'SW'), (1, 1, 'SE')]
valid_directions = deque([(-1, 0, 'N'), (1, 0, 'S'), (0, -1, 'W'), (0, 1, 'E')])

#    ___     _     _      _ _                  
#   / __|___| |_  (_)_ _ (_) |_   _ __  ___ ___
#  | (_ / -_)  _| | | ' \| |  _| | '_ \/ _ (_-<
#   \___\___|\__| |_|_||_|_|\__| | .__/\___/__/
#                                |_|           

def get_init_pos_elves(matrix: list) -> list:
    elves = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                elves.append((i,j))
    return elves

#    ___  _  _ ___   ___  ___  _   _ _  _ ___    _  _   _   _  _ ___  _    ___ ___ 
#   / _ \| \| | __| | _ \/ _ \| | | | \| |   \  | || | /_\ | \| |   \| |  | __| _ \
#  | (_) | .` | _|  |   / (_) | |_| | .` | |) | | __ |/ _ \| .` | |) | |__| _||   /
#   \___/|_|\_|___| |_|_\\___/ \___/|_|\_|___/  |_||_/_/ \_\_|\_|___/|____|___|_|_\

def consider_move(grid, i, j):
    for dx, dy, direction in valid_directions: # directions define here as global variable
        
        if 0 <= i + dx <= height and 0 <= j + dy <= width:
            try:
                if not any(grid[i+di][j+dj] == ELF for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)] if i+di >= 0 and i+di <= height and j + dj >= 0 and j + dj <= width):
                    return None

                elif grid[i + dx][j + dy] == GROUND:
                    if (direction == 'N' or direction == 'S') and grid[i + dx][j + 1 + dy] == GROUND and grid[i + dx][j - 1 + dy] == GROUND: 
                        return (i + dx, j + dy)

                    if (direction == 'W' or direction == 'E') and grid[i + 1 + dx][j + dy] == GROUND and grid[i - 1 + dx][j + dy] == GROUND:
                        return (i + dx, j + dy)
            except:
                continue

    return None # no valide moves found

def one_round_move_elves(grid, elves, round):
    flag = 0
    elves_check = copy.deepcopy(elves)
    # proposed_moves keys will be the proposed moves, and the value the initial value of elves before moving
    proposed_moves = {} # reset dict for each ROUND
    for i, j in elves:
        proposed_destination = consider_move(grid, i, j)

        if proposed_destination:
            if proposed_destination in proposed_moves:
                proposed_moves[proposed_destination].append((i, j))
            else:
                proposed_moves[proposed_destination] = [(i, j)]

    for new_pos in proposed_moves:
        if (len(proposed_moves[new_pos])) == 1:
            xinit, yinit = proposed_moves[new_pos][0]
            xnew, ynew = new_pos
            grid[xinit] = grid[xinit][:yinit] + '.' + grid[xinit][yinit + 1:]
            grid[xnew]  = grid[xnew][:ynew] + '#' + grid[xnew][ynew + 1:]
            index = next(i for i, pos in enumerate(elves) if pos[0] == xinit and pos[1] == yinit)
            elves[index] = (xnew, ynew)
            t=1
    if (round + 1) == 903:
        t=1
    if set(elves_check) == set(elves):
        print(f"The first round where no elves moves is: {round + 1}")
        flag = 1
    return grid, elves, flag

def count_empty_ground_tiles(grid):
    # Find the minimum and maximum row and column indices that contain an elf
    min_row, max_row = float('inf'), -float('inf')
    min_col, max_col = float('inf'), -float('inf')

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ELF:
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)
    
    # Count the number of empty ground tiles in the rectangle
    count = 0
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if grid[i][j] == GROUND:
                count += 1
    
    return count 

#   __  __   _   ___ _  _ 
#  |  \/  | /_\ |_ _| \| |
#  | |\/| |/ _ \ | || .` |
#  |_|  |_/_/ \_\___|_|\_|
                        
if __name__ == '__main__':

    filename = "23.in"
    with open(filename, 'r') as f:
        datas = f.read().strip().split("\n")

    width  = len(datas[0])
    height = len(datas)
    elves = get_init_pos_elves(datas)
    nb_round = 1000

    for round in range(nb_round):
        datas, elves, flag = one_round_move_elves(datas, elves, round)
        valid_directions.rotate(-1)
        if flag == 1:
            break
    count_nb_tiles = count_empty_ground_tiles(datas)
    print(f"First part: There is {count_nb_tiles} empty ground tiles for {round + 1} rounds")
    print(f"Second part: The first round where elves stop moving is {round + 1}")


