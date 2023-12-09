filename = "8.in"

instructions, _, *data = open(filename).read().splitlines()
network = {}

for l in data:
    node, possibilities = l.split(' = ')
    network[node] = possibilities[1:-1].split(', ')

counter = 0
position = "AAA"

while position != "ZZZ":
    counter += 1

    if instructions[0] == "L":
        position = network[position][0]
    else:
        position = network[position][1]
    instructions = instructions[1:] + instructions[0]

print(counter)