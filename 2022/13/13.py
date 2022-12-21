with open("13.in") as f:
    datas = f.read().strip().split("\n\n")


def compare_packets(a, b):
    # Convert integers to lists containing that integer
    if isinstance(a, int) and isinstance(b, int):
        if a < b: # Stop the comparison and return true
            return True
        if a == b:
            return "continue" # Continue
        else:
            return -1
    if isinstance(a, list) and isinstance(b, int):
        b = [b]

    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            data = compare_packets(a[i], b[i])
            if data == 1:
                return True
            if data == -1:
                return -1
            i += 1

        if i == len(a):
            if len(a) == len(b):
                return "hard_to_continue_here"
            return True

        return -1
    # Compare the packets, element by element

    # If we reach this point, the packets are in the b order

# Test the function with the example packets
# pairs = [
#     ([1,1,3,1,1], [1,1,5,1,1]),
#     ([[1], [2,3,4]], [[1], 4]),
#     ([9], [[8,7,6]]),
#     ([[4,4],4,4], [[4,4],4,4,4]),
#     ([7,7,7,7], [7,7,7]),
#     ([], [3]),
#     ([[[]]], [[]]),
#     ([1, [2, [3, [4, [5,6,7]]]], 8, 9], [1, [2, [3, [4, [5,6,0]]]], 8, 9])
# ]
#   ___  _   ___ _____   _ 
#  | _ \/_\ | _ \_   _| / |
#  |  _/ _ \|   / | |   | |
#  |_|/_/ \_\_|_\ |_|   |_|
                         
                         
good_index = []
result = 0
for i, packet in enumerate(datas):
    a, b = map(eval, packet.split("\n"))
    
    if compare_packets(a, b) == True:
        result += i + 1
        
print(f"There are {result} pairs of packets in the right order.")

#   ___  _   ___ _____   ___ 
#  | _ \/_\ | _ \_   _| |_  )
#  |  _/ _ \|   / | |    / / 
#  |_|/_/ \_\_|_\ |_|   /___|
from functools import cmp_to_key

first_divider_packet = [[2]]
second_divider_packet = [[6]]

with open("13.in") as f:
    datas = f.read().strip().replace("\n\n", "\n").split("\n")                        
datas_list = list(map(eval, datas))
datas_list.append(first_divider_packet)
datas_list.append(second_divider_packet)

# It tooks the end of datas_list and take each line a will be datas_list[-1] and b datas_list[-2]
# next turn it will be a = datas_list[-3] and b = datas_list[-4]
datas_list = sorted(datas_list, key=cmp_to_key(compare_packets), reverse=True)

for i, val in enumerate(datas_list):
    if val == first_divider_packet:
        a = i + 1
    if val == second_divider_packet:
        b = i + 1

print(f"The decoder key is: {a * b}")