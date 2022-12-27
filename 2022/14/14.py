from collections import defaultdict


filename = "14.in"
elements = set()
abyss = 0

#     __  __                       __    __                                       __                             _            __         
#    / / / /  ____ _   ____   ____/ /   / /  ___           _____  ____   _____   / /__           ____   ____    (_)   ____   / /_   _____
#   / /_/ /  / __ `/  / __ \ / __  /   / /  / _ \         / ___/ / __ \ / ___/  / //_/          / __ \ / __ \  / /   / __ \ / __/  / ___/
#  / __  /  / /_/ /  / / / // /_/ /   / /  /  __/        / /    / /_/ // /__   / ,<            / /_/ // /_/ / / /   / / / // /_   (__  ) 
# /_/ /_/   \__,_/  /_/ /_/ \__,_/   /_/   \___/        /_/     \____/ \___/  /_/|_|          / .___/ \____/ /_/   /_/ /_/ \__/  /____/  
#                                                                                            /_/  
#                                        
for line in open(filename, 'r'):
    datas = [list(map(int, points.split(','))) for points in line.strip().split(" -> ")]

    for (x1, y1), (x2, y2) in zip(datas, datas[1:]): # generate a tuple of 
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                elements.add(x + y * 1j)
                abyss = max(abyss, y + 1)
total = 0
floor = int(max(elements, key=lambda y: y.imag).imag) + 2
for x in range(200, 800): # Arbitrary values
    elements.add(x + floor * 1j)

#    _____    _                         __           __                                             __           ____            __    __    _                  
#   / ___/   (_)   ____ ___   __  __   / /  ____ _  / /_  ___           _____  ____ _   ____   ____/ /          / __/  ____ _   / /   / /   (_)   ____    ____ _
#   \__ \   / /   / __ `__ \ / / / /  / /  / __ `/ / __/ / _ \         / ___/ / __ `/  / __ \ / __  /          / /_   / __ `/  / /   / /   / /   / __ \  / __ `/
#  ___/ /  / /   / / / / / // /_/ /  / /  / /_/ / / /_  /  __/        (__  ) / /_/ /  / / / // /_/ /          / __/  / /_/ /  / /   / /   / /   / / / / / /_/ / 
# /____/  /_/   /_/ /_/ /_/ \__,_/  /_/   \__,_/  \__/  \___/        /____/  \__,_/  /_/ /_/ \__,_/          /_/     \__,_/  /_/   /_/   /_/   /_/ /_/  \__, /  
#                                                                                                                                                      /____/   
while True:
    # New round
    sand = 500
    while True:
        # Check if there is already a sand or a rock
        if sand.imag >= floor:
            break
        if sand + 1j not in elements:
            sand += 1j
            continue
        if sand + 1j - 1 not in elements:
            sand += 1j - 1
            continue
        if sand + 1j + 1 not in elements:
            sand += 1j + 1
            continue
        break

    elements.add(sand)
    total += 1
    
    if sand.imag == 0: # it means that the sand can not go down
        x_min = int(min(elements, key=lambda x: x.real).real)
        x_max = int(max(elements, key=lambda x: x.real).real)

        print(f"PART 2: total sands stuck in the cave: {total}")

        # Get a visualization of the final results
        for y in range(floor + 1):
            for x in range(x_min, x_max):
                if x + y * 1j in elements:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

        exit(0) # exit the main while True loop

t=2
           
    