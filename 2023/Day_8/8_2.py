import math

filename = "8.in"

instructions, _, *data = open(filename).read().splitlines()
network = {}
nb_steps = []
start = "A"
end = "Z"


for l in data:
    node, possibilities = l.split(' = ')
    network[node] = possibilities[1:-1].split(', ')

def compute_step_end_z(start, end, instructions, network):
    counter_steps = 0
    position = start
    while position[2] != end:
        counter_steps += 1
        if instructions[0] == "L":
            position = network[position][0]
        else:
            position = network[position][1]
        instructions = instructions[1:] + instructions[0]
    return counter_steps

net_starts = [n for n in list(network.keys()) if n[2] == start]

for ns in net_starts:
    nb_steps.append(compute_step_end_z(ns, end, instructions, network))
# There, we have the loop of each starts. We have to know the lowest common of each start
# We know that the lowest common denominator will be the moment where everything is ending at "Z" point
response = math.lcm(*nb_steps)
print(f"Part 2: {response}")
