from collections import defaultdict, deque

filename = "5.in"

tuple_orders = []
instructions_list = []

with open(filename, 'r') as file:
    input = file.read().splitlines()  # Read the expression from the file


for item in input:
    if '|' in item:
        # Transformer les éléments séparés par '|' en tuples
        tuple_orders.append(tuple(map(int, item.split('|')))) # <=> tuples_list.append(tuple(int(val) for val in item.split('|')))
    elif ',' in item:
        # Transformer les éléments séparés par ',' en listes
        instructions_list.append(list(map(int, item.split(','))))

# Construire un graphe des dépendances
graph = defaultdict(list)  # Un dictionnaire de listes pour les voisins
in_degree = defaultdict(int)  # Dictionnaire pour les degrés entrants (nombre de dépendances)

# Initialiser les noeuds du graphe (les pages)
for a, b in tuple_orders:
    graph[a].append(b)  # Ajouter b comme voisin de a
    in_degree[b] += 1  # Augmenter le degré entrant de b
    if a not in in_degree:
        in_degree[a] = 0  # Assurer que a a un degré entrant de 0 (si c'est la première fois qu'on le voit)

# Appliquer un algorithme de tri topologique (Kahn's Algorithm)
def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])  # Commencer avec les noeuds sans dépendance
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_order

sorted_pages = topological_sort(graph, in_degree)

def is_instruction_in_order(main_list, instruction):
    instr_idx = 0

    for el in main_list:
        if el == instruction[instr_idx]:
            instr_idx += 1
        if instr_idx == len(instruction):
            return True
    return False

middle_elements = [
    instruction[len(instruction) // 2]
    for instruction, valid in zip(instructions_list, [is_instruction_in_order(sorted_pages, instructions_list[i])
    for i in range(len(instructions_list))]) if valid
]

print(f"Résultat partie 1: {sum(middle_elements)}")

