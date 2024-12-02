import numpy as np

filename = r'1.in'
with open(filename, 'r') as f:
    first_list, second_list = zip(*(
        map(int, line.split()) for line in f if line.strip()
    ))

#    __ _        _                    _
#   / _(_)_ _ __| |_   _ __  __ _ _ _| |_
#  |  _| | '_(_-<  _| | '_ \/ _` | '_|  _|
#  |_| |_|_| /__/\__| | .__/\__,_|_|  \__|
#                     |_|
first_part_result  = 0
first_list_sorted  = np.sort(first_list)
second_list_sorted = np.sort(second_list)

if len(first_list_sorted) == len(second_list_sorted):
    for i in range(len(first_list_sorted)):
        first_part_result += np.abs(first_list_sorted[i] - second_list_sorted[i])
print(first_part_result)

#                          _                  _
#   ___ ___ __ ___ _ _  __| |  _ __  __ _ _ _| |_
#  (_-</ -_) _/ _ \ ' \/ _` | | '_ \/ _` | '_|  _|
#  /__/\___\__\___/_||_\__,_| | .__/\__,_|_|  \__|
#                             |_|

second_part_result = 0
for i in range(len(first_list)):
    val_first_list = first_list[i]
    val_second_list = second_list[i]

    second_part_result += val_first_list * second_list.count(val_first_list)
print(second_part_result)
