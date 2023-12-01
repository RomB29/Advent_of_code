filename = r'1_1.in'
with open(filename, 'r') as f:
    lines = f.read().strip().split()

array = []
output = 0
for line in lines:
    temp_array = []
    for character in line:
        try:
            temp_array.append(int(character))
        except ValueError:
            pass
    if temp_array:
        output = output + (int(str(temp_array[0]) + str(temp_array[-1])))
print(f"The result is: {output}")