from collections import defaultdict, Counter

buyers = []
with open("22.in") as f:
    for line in f:
        buyers.append(int(line.strip()))

def mix(secret_number, val):
    secret_number ^= val
    return secret_number

def prune(secret_number):
    secret_number %= 16777216
    return secret_number

def steps(secret_number):
    step_1 = secret_number * 64
    secret_number = prune(mix(secret_number, step_1))
    step_2 = secret_number // 32
    secret_number = prune(mix(secret_number, step_2))
    step_3 = secret_number * 2048
    secret_number = prune(mix(secret_number, step_3))

    return secret_number

def get_last_digit(number):
    return int(str(number)[-1])

def get_diff(old_val, new_val):
    return new_val - old_val

def update_sequence(sequence):
    new_sequence = []
    for i, val in enumerate(sequence):
        if i == 0:
            new_sequence.append(get_last_digit(sequence[i] + sequence[-1]))
        else:
            new_sequence.append(get_last_digit(sequence[i] + sequence[i - 1]))
    return new_sequence


sequence = [[] for _ in range(len(buyers))]


for i in range(2000):
    for i_b, val_b in enumerate(buyers):
        temp = get_last_digit(val_b)
        if i > 0:
            diff = get_diff(sequence[i_b][i - 1][0], temp)
        else:
            diff = 0
        sequence[i_b].append((temp, diff))
        buyers[i_b] = steps( buyers[i_b])
        t=1

part_1 = sum(buyers)
print(f"Résultat partie 1: {part_1}")


# # List of tuples
# list1 = [(3, 1), (0, -3), (2, 6), (5, -2), (4, -2), (4, 0), (6, 2), (4, -4), (4, 0), (2, -2)]
# list2 = [(3, 0), (0, -3), (6, 6), (5, -1), (4, -1), (4, 0), (6, 2), (4, -4), (4, 0), (2, -2)]

# Combine the lists



patterns = []
test = []
for seq in sequence:
    tuple0_values = [t[0] for t in seq]
    tuple1_values = [t[1] for t in seq]
    patterns.append([(tuple0_values[i - 1], tuple(tuple1_values[i-4: i])) for i in range(3, len(tuple1_values))])
    test.append([tuple(tuple1_values[i-4: i]) for i in range(3, len(tuple1_values))])
    t=1


pattern_counts = defaultdict(int)
value_sums = defaultdict(int)

for pattern_set in patterns:
    temp_set = set()
    for value, pattern in pattern_set:
        if pattern not in temp_set:
            pattern_counts[pattern] += 1
            value_sums[pattern] += value
            temp_set.add(pattern)

sorted_value_sums = sorted(
    (item for item in value_sums.items() if len(item[0]) > 0),
    key = lambda x: x[1],
    reverse=True
)

print(f"Résultat partie 2: {sorted_value_sums[0][1]}")
