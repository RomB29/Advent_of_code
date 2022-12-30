filename = "17.in"
rocks = [
    [0, 1, 2 ,3],
    [1j, 1, 1 + 1j, 1 + 2j, 2 + 1j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]

with open(filename, 'r') as f:
    datas = f.read().strip()

seen = {}
jets = [1 if x == ">" else -1 for x in datas]
solid = {x - 1j for x in range(7)} # it is the floor
height = 0

rock_count = 0
rock_index = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]} # Because the starting point is 2 unit from the left side and 3 unit above the top of the structure


while rock_count < 2022:
    for jet in jets:
        moved = {x + jet for x in rock}
        # Using all or any
        # >>> all([True, True, True])
        # True
        # >>> all([True, False, True])
        # False
        # >>> all([])
        # True

        # # Using any
        # >>> any([True, True, True])
        # True
        # >>> any([True, False, True])
        # True
        # >>> any([False, False, False])
        # False
        # >>> any([])
        # False

        if all(0 <= x.real < 7 for x in moved) and not (moved & solid): 
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock # equivalent to solid = solid | rock  which | is "or"

            rock_count += 1
            height = max(x.imag for x in solid) + 1
            if rock_count >= 2022:
                break

            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}


        else:
            rock = moved

print(f"Part 1: The height of the tower is: {int(height)}")
