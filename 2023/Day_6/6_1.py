filename = "6.in"

with open(filename, 'r') as f:
    data = f.read().strip().split(':')
    header_time = data[0]
    data_time = list(map(int, data[1].strip().split("\n")[0].split()))
    header_distance = data[1].strip().split("\n")[1]
    data_distance = list(map(int, data[2].strip().split()))

data = {
    header_time: data_time,
    header_distance: data_distance
}

nb_world_records = []
for i_race, val_race in enumerate(data[header_time]):
    race_test = []
    possibilities = []
    temp_race = val_race
    hold_button = 1
    for poss in range(temp_race):
        temp_distance = []


        for i in range(temp_race):
            temp_distance.append(i*hold_button)
        possibilities.append(temp_distance[-1])
        hold_button += 1
        temp_race -= 1
    nb_world_records.append([val for val in possibilities if val > data_distance[i_race]])

result = 1
for nb_records in nb_world_records:
    result *= len(nb_records)
print(f"Résultat part 1: {result}")