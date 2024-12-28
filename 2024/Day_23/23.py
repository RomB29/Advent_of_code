from collections import defaultdict
from itertools import combinations

data = [line.strip().split("-") for line in open("23.in")]


def get_computer_names(data):
    unique_names = set()
    for pair in data:
        unique_names.update(pair)
    return list(unique_names)

def get_connections(computer, data):
    computer_connections = set()
    for i_d, val_d in enumerate(data):
        if computer in data[i_d]:
            computer_connections.update(val_d)
    computer_connections.remove(computer)
    return list(computer_connections)

connections = {}
computer_names = get_computer_names(data)
for cn in computer_names:
    connections[cn] = get_connections(cn, data)


# Fonction pour vérifier les interconnections
def get_interconnections(connections):
    sets = set()
    for x in connections:
        for y in connections[x]:
            for z in connections[y]:
                if x != z and x in connections[z]:
                    sets.add(tuple(sorted([x, y, z])))
    return sets
sets = get_interconnections(connections)

ans = len([s for s in sets if any(c.startswith("t") for c in s)])
print(ans)

# Part 2
networks = [{c} for c in computer_names]
tuple_data = {tuple([a, b]) for a, b in data}

extended_data = [(a, b) for a, b in tuple_data] + [(b, a) for a, b in tuple_data]

for n in networks:
    for c in computer_names:
        if all((c, d) in extended_data for d in n):
            n.add(c)

longest_network = max(networks, key=len)
sorted_network = sorted(longest_network)

print(f"{','.join(sorted_network)}")
t=1