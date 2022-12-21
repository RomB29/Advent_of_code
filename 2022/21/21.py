from sympy import symbols, solve_linear
from sympy.parsing.sympy_parser import parse_expr

filename = "21.in"

all_monkeys = {}

with open(filename, 'r') as f:
    datas = f.read().strip().split("\n")

for line in datas:
    parts = line.split(" ")
    monkey = parts[0][:-1] # Take everything excepted ":"

    if (len(parts) == 2):
        all_monkeys[monkey] = int(parts[1])
    else:
        all_monkeys[monkey] = parts[1:]

def compute_part_1(the_monk):
    if isinstance(all_monkeys[the_monk], int):
        return all_monkeys[the_monk]

    parts = all_monkeys[the_monk]
    left = compute_part_1(parts[0])
    right = compute_part_1(parts[2])

    return eval(f"{left}{parts[1]}{right}")

#   ___     _     ___   _____     _ 
#  | _ \   /_\   | _ \ |_   _|   / |
#  |  _/  / _ \  |   /   | |     | |
#  |_|   /_/ \_\ |_|_\   |_|     |_|
                                  

res = int(compute_part_1("root"))
print(f"root_monkey_number = {res}")
t=1

#   ___     _     ___   _____     ___ 
#  | _ \   /_\   | _ \ |_   _|   |_  )
#  |  _/  / _ \  |   /   | |      / / 
#  |_|   /_/ \_\ |_|_\   |_|     /___|

humnn_is_me = symbols("humn") 
                           
def compute_part_2(the_monk):

    if the_monk == "humn":
        return humnn_is_me

    if isinstance(all_monkeys[the_monk], int):
        return all_monkeys[the_monk]

    parts = all_monkeys[the_monk]
    left = compute_part_2(parts[0])
    right = compute_part_2(parts[2])

    return parse_expr(f"({left}){parts[1]}({right})")     
   
left = compute_part_2(all_monkeys["root"][0])
right = compute_part_2(all_monkeys["root"][2])   

print(f"The equation is: {left} = {right}")
res2 = solve_linear(left, right)[1]
print(f"I should yell {res2} for the equality")
t=1