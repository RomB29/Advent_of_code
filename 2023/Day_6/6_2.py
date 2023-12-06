import math

filename = "6.in"

with open(filename, 'r') as f:
    data = f.read().strip().split(':')
    header_time = data[0]

    data_time = data[1].strip().split()
    last_element = data_time.pop()
    data_time = int(''.join(data_time))
    header_distance = data[1].strip().split("\n")[1]
    data_distance = int(''.join(data[2].strip().split()))

data = {
    header_time: data_time,
    header_distance: data_distance
}


low = math.ceil(data[header_distance] / data[header_time])
high = data[header_time] - low

solution = 1
poss = 0
for hold in range(data_time):
    if hold * (data_time - hold) > data_distance:
        poss += 1
solution *= poss

print(f"Part 2 solution is: {solution}")