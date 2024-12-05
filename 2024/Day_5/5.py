filename = "5.in"

tuple_orders = []
list_update = []

with open(filename, 'r') as file:
    input = file.read().splitlines()


for item in input:
    if '|' in item:
        tuple_orders.append(tuple(map(int, item.split('|')))) # <=> tuples_list.append(tuple(int(val) for val in item.split('|')))
    elif ',' in item:
        list_update.append(list(map(int, item.split(','))))

cache = {}

for x, y in tuple_orders:
    cache[(x, y)] = True
    cache[(y, x)] = False


def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and cache[key]:
                return False
    return True

res = 0
for update in list_update:
    if is_ordered(update):
        res += update[len(update) // 2]
print(f"Résultat partie 1: {res}")