from collections import deque

filename = "./input.in"
N = 9 # Line
drawing_lines = 8 # Row

def read_file(filename):
    with open(filename) as f:
    # Parsing the data
        parts = f.read().split("\n\n")
        drawing = parts[0].split("\n")


        stacks = [[] for _row in range(N)]
        for i in range(drawing_lines):
            line = drawing[i]
            crates = line[1::4]
            for s in range(len(crates)):
                if crates[s] != " ":
                    stacks[s].append(crates[s])
        # Get all list of stacks
        stacks = [stack[::-1] for stack in stacks]
    return stacks, parts

## Lets start the move of the cranes

#   ___                _       _   
#  | _ \  __ _   _ _  | |_    / |  
#  |  _/ / _` | | '_| |  _|   | |  
#  |_|   \__,_| |_|    \__|   |_|  

stacks, parts = read_file(filename)

for line in parts[1].split("\n"):
    # Split all commands 
    actions = line.split(" ")
    nb_crates_to_move = int(actions[1])
    origin            = int(actions[3])
    destination       = int(actions[5])

    in_stack_to_move      = stacks[origin - 1][(len(stacks[origin - 1]) - nb_crates_to_move):]
    in_stack_after_moving = stacks[origin - 1][: len(stacks[origin - 1]) - nb_crates_to_move]
    try:
        stacks[destination - 1].extend(in_stack_to_move.reverse())
    except:
        stacks[destination - 1].extend(in_stack_to_move)
    

    stacks[origin - 1] = in_stack_after_moving


messages = [var[-1] for var in stacks]


print(f"The crates that ends up on top of each stack is {''.join(messages)} - CrateMover 9000")


#   ___                _       ___ 
#  | _ \  __ _   _ _  | |_    |_  )
#  |  _/ / _` | | '_| |  _|    / / 
#  |_|   \__,_| |_|    \__|   /___|

stacks, parts = read_file(filename)

for line in parts[1].split("\n"):
    # Split all commands 
    actions = line.split(" ")
    nb_crates_to_move = int(actions[1])
    origin            = int(actions[3])
    destination       = int(actions[5])

    in_stack_to_move      = stacks[origin - 1][(len(stacks[origin - 1]) - nb_crates_to_move):]
    in_stack_after_moving = stacks[origin - 1][: len(stacks[origin - 1]) - nb_crates_to_move]
    try:
        stacks[destination - 1].extend(in_stack_to_move)
    except:
        stacks[destination - 1].extend(in_stack_to_move)
    

    stacks[origin - 1] = in_stack_after_moving


messages = [var[-1] for var in stacks]

print(f"The crates that ends up on top of each stack is {''.join(messages)} - CrateMover 9001")
