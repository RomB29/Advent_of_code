import functools

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
    cache[(x, y)] = -1
    cache[(y, x)] = 1


def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and cache[key] == 1:
                return False
    return True

def cmp(x, y):
    return cache.get((x, y), 0) # could be anything else than 0

res = 0
for update in list_update:
    if is_ordered(update): continue
    update.sort(key=functools.cmp_to_key(cmp))
    res += update[len(update) // 2]
print(f"Résultat partie 1: {res}")