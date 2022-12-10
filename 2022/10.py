file_path = "input.in"
from typing import List

datas = []
# initialize the list of cycles at which to calculate the signal strength
interesting_cycles = [20, 60, 100, 140, 180, 220] #PART 1
# initialize the signal strength sum to 0
signal_strength_sum = 0

grid_prompt = [['?' for _ in range(40)] for _ in range(6)] # PART 2

with open(file_path) as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("\r", "")
        line = line.replace("\t", "")
        datas.append(line)
        
def check_cycles(cycle, x, signal_strength_sum): #PART 1
    if cycle in interesting_cycles:
        signal_strength = cycle * x
        signal_strength_sum += signal_strength
        print(f"x = {x}")
        print(f"s_s = {signal_strength}")
        print(f"signal_strength_sum = {signal_strength_sum}")
        return signal_strength_sum
    else:
        return signal_strength_sum

def update_grid_prompt(cycle: int, x: int, grid_prompt: List[List[str]]) -> List[List[str]]: # PART 2
    """
    Update the grid prompt with the current sprite position.

    :param cycle: The current cycle number.
    :param x: The current position of the middle of the sprite on the horizontal axis.
    :param grid_prompt: The current state of the grid prompt.
    :return: The updated grid prompt.
    """
    sprite_range = range(x-1, x+2)
    if (cycle - 1) % 40 in sprite_range:
        grid_prompt[(cycle - 1) // 40][(cycle - 1) % 40] = '#'
    else:
        try:
            grid_prompt[(cycle - 1) // 40][(cycle - 1) % 40] = ' '
        except:
            grid_prompt[0][(cycle - 1) % 40] = ' '
    return grid_prompt

# initialize the register X to 1
x = 1

# initialize the cycle counter to 1
cycle = 1


# simulate the execution of the program
for i_instr, instruction in enumerate(datas):
    # parse the current instruction
    instruction = datas[i_instr]

    if "addx" in instruction:
        op, arg = instruction.split()
        arg = int(arg)
        cycle += 1

        grid_prompt = update_grid_prompt(cycle, x, grid_prompt)
        x += arg
        cycle += 1

        grid_prompt = update_grid_prompt(cycle, x, grid_prompt)

        signal_strength_sum = check_cycles(cycle, x, signal_strength_sum)

    else: # noop instruction
        cycle += 1

        grid_prompt = update_grid_prompt(cycle, x, grid_prompt)
        signal_strength_sum = check_cycles(cycle, x, signal_strength_sum)
    
        # calculate the signal strength for the current cycle if it is in the interesting_cycles set

# print the sum of the signal strengths at the interesting cycles
print('\n'.join([''.join(row) for row in grid_prompt]))
print(signal_strength_sum)

