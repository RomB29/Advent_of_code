file_path = "input_1.txt"

file = open(file_path, "r")
data = []
tentative = []
for line in file:
  stripped_line = line.rstrip()
  data.append(stripped_line.split(','))


count = 0
overlapping = 0

for group in data:
    a = int(group[0].split('-')[0])
    b = int(group[0].split('-')[1])

    c = int(group[1].split('-')[0])
    d = int(group[1].split('-')[1])
    
    if a <= c and b >= d or a >= c and b <= d: # part 1
        count += 1

    # a----b  c----d -> not overlapping
    # c----d  a----b -> not overlapping
    if not(b < c or d < a): # part 2
        overlapping += 1
        
print("Number of pairs which fully contain the other: {}".format(count))
print("Overlapping pairs: {}".format(overlapping))
