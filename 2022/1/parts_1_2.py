# ██████   █████  ██████  ████████      ██ 
# ██   ██ ██   ██ ██   ██    ██        ███ 
# ██████  ███████ ██████     ██         ██ 
# ██      ██   ██ ██   ██    ██         ██ 
# ██      ██   ██ ██   ██    ██         ██ 
                                         
                                         
filepath = 'input_1_2.txt'

cnt = 1
elves = 0
temp_count = []
tuple_elfes = []
temp_max = 0

with open(filepath) as fp:
    line = fp.readline()

    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1

        if line not in ['\n', '\r\n', '']:
            temp_count.append(int(line.strip()))
        if line == "\n":
            elves += 1
            if sum(temp_count) > temp_max:
                temp_max = sum(temp_count)
            tuple_elfes.append((elves, sum(temp_count)))
            temp_count = []
            print("Elves: {}".format(elves))

max_tuple_1 = max(tuple_elfes, key=lambda tup: tup[1])
print("l'elfe n°{} a récolté un max de calories -> {} !!".format(max_tuple_1[0], max_tuple_1[1]))


# ██████   █████  ██████  ████████     ██████  
# ██   ██ ██   ██ ██   ██    ██             ██ 
# ██████  ███████ ██████     ██         █████  
# ██      ██   ██ ██   ██    ██        ██      
# ██      ██   ██ ██   ██    ██        ███████ 
# 

tuple_elfes.remove(max_tuple_1)  

max_tuple_2 = max(tuple_elfes, key=lambda tup: tup[1])
tuple_elfes.remove(max_tuple_2) 

max_tuple_3 = max(tuple_elfes, key=lambda tup: tup[1])
tuple_elfes.remove(max_tuple_3)

total_1_2_3_elfes = max_tuple_1[1] + max_tuple_2[1] + max_tuple_3[1]
print("les 3 premiers elfes ont récoltés -> {} calories!!".format(total_1_2_3_elfes))

t=1                                            
                                        