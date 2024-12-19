from functools import cache

data = open("19.in").read().strip().split("\n\n")


patterns = data[0].split(",")
patterns = [pattern.strip() for pattern in patterns]

towels = data[1].split("\n")

@cache
def valid_target(towel:str) -> bool:
    if towel == "":
        return 1
    count = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            count += valid_target(towel[len(pattern):])

    return count

sol = 0
for i, val in enumerate(towels):
    sol += valid_target(val)
    t=1

print(f"Solution partie 2: {sol}")