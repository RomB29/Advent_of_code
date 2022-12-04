file_path = "input_1.txt"
lines_list = []
data = []
scoring = {'a':1, 'b':2, 'c':3, 'd':4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 
    'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
total_score   = 0
total_score_2 = 0

## READ FILE TO LIST
file = open(file_path, "r")
for line in file:
  stripped_line = line.strip()
  lines_list.append(stripped_line)


# ██████   █████  ██████  ████████      ██ 
# ██   ██ ██   ██ ██   ██    ██        ███ 
# ██████  ███████ ██████     ██         ██ 
# ██      ██   ██ ██   ██    ██         ██ 
# ██      ██   ██ ██   ██    ██         ██ 
                                         
                                         
for line in lines_list:
    temp1 = []
    temp2 = []

    for var in line[0:int(len(line)/2)]:
        temp1.append(var)
    for var in line[int(len(line)/2):]:
        temp2.append(var)   
        
    for val1 in temp1:
        if val1 in temp2:
            data.append(val1)
            break

total_score = sum([scoring[char] for char in data])
print("Sum prioritize: {}".format(total_score))


# ██████   █████  ██████  ████████     ██████  
# ██   ██ ██   ██ ██   ██    ██             ██ 
# ██████  ███████ ██████     ██         █████  
# ██      ██   ██ ██   ██    ██        ██      
# ██      ██   ██ ██   ██    ██        ███████ 
i=0
data_part2 = []

while i < len(lines_list):
    for line in lines_list[i:i+3]:
        try:
            for val in lines_list[i]:
                if (val in lines_list[i+1] and val in lines_list[i+2]):
                    data_part2.append(val)
                    i += 3 
                    break
        except:
            pass
       

total_score_2 = sum([scoring[char] for char in data_part2])
print("Sum prioritize: {}".format(total_score_2))  
