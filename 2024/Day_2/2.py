import numpy as np

filename = r'2.in'
with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')

data_parsed = [list(map(int, lines[i].split())) for i in range(len(lines))]
result = 0

for i in range(len(data_parsed)):
    diff  = np.diff(data_parsed[i])
    signs = np.sign(diff)
    flag = 1
    for j in range(len(diff)):
        if np.abs(diff[j]) >= 1 and np.abs(diff[j]) <= 3 and np.all(signs == signs[0]):
            pass
        else:
            flag = 0
            break
    if flag == 0:
        continue
    else:
        result += 1

print(f"Le résultat de la partie 1 est: {result}")

result = 0

for i in range(len(data_parsed)):
    diff  = np.diff(data_parsed[i])
    signs = np.sign(diff)
    flag = 1
    for j in range(len(diff)):
        if np.abs(diff[j]) >= 1 and np.abs(diff[j]) <= 3 and signs[j] == signs[0]:
            pass

        else:
            flag = 0
            break

    if flag == 0:
        for j in range(len(data_parsed[i])):
            trimmed_line = data_parsed[i][:j] + data_parsed[i][j+1:]  # Remove element at index j
            new_diff = np.diff(trimmed_line)
            new_signs = np.sign(new_diff)

            # Check if differences are safe for the trimmed line
            if all(1 <= np.abs(g) <= 3 and new_signs[0] == new_signs[k] for k, g in enumerate(new_diff)):
                flag = 1
                break
    if flag == 1:
        result += 1

print(f"Le résultat de la partie 2 est: {result}")

