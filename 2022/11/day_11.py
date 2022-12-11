from itertools import count
import heapq
import math

"""
Explanation part2

The least common multiple (LCM) of two or more numbers is the smallest positive integer that is a multiple of all the numbers. For example, the LCM of 3 and 4 is 12, since 12 is the smallest positive integer that is a multiple of both 3 and 4.

To calculate the LCM of two numbers, you can use the following formula:

Copy code
LCM(a, b) = |a * b| / gcd(a, b)
Where a and b are the two numbers, |a * b| is the absolute value of the product of a and b, and gcd(a, b) is the greatest common divisor of a and b.

For example, to calculate the LCM of 15 and 20, you can use the following steps:

Calculate the absolute value of the product of 15 and 20, which is |15 * 20| = 300. (in this case 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
Calculate the greatest common divisor of 15 and 20, which is gcd(15, 20) = 5. (in this case it depends of the value of the item)
Divide the result from step 1 by the result from step 2, which gives 300 / 5 = 60.
Therefore, the LCM of 15 and 20 is 60.
"""

lcm = 1 # LEAST COMMUN MULTIPLE
modu = [2, 3, 5, 7, 11, 13, 17, 19]
for x in modu:
    lcm = (lcm * x) # MOD
# Define the attributes of each monkey
monkey0 = {
    "starting_items": [54, 61, 97, 63, 74],
    "operation": lambda x: x * 7,
    "test": lambda x: x % 17 == 0,
    "if_true": 5,
    "if_false": 3,
    "nb_actions": 0
}

monkey1 = {
    "starting_items": [61, 70, 97, 64, 99, 83, 52, 87],
    "operation": lambda x: x + 8,
    "test": lambda x: x % 2 == 0,
    "if_true": 7,
    "if_false": 6,
    "nb_actions": 0
}

monkey2 = {
    "starting_items": [60, 67, 80, 65],
    "operation": lambda x: x * 13,
    "test": lambda x: x % 5 == 0,
    "if_true": 1,
    "if_false": 6,
    "nb_actions": 0
}

monkey3 = {
    "starting_items": [61, 70, 76, 69, 82, 56],
    "operation": lambda x: x + 7,
    "test": lambda x: x % 3 == 0,
    "if_true": 5,
    "if_false": 2,
    "nb_actions": 0
}

monkey4 = {
    "starting_items": [79, 98],
    "operation": lambda x: x + 2,
    "test": lambda x: x % 7 == 0,
    "if_true": 0,
    "if_false": 3,
    "nb_actions": 0
}
monkey5 = {
    "starting_items": [72, 79, 55],
    "operation": lambda x: x + 1,
    "test": lambda x: x % 13 == 0,
    "if_true": 2,
    "if_false": 1,
    "nb_actions": 0
}

monkey6 = {
    "starting_items": [63],
    "operation": lambda x: x + 4,
    "test": lambda x: x % 19 == 0,
    "if_true": 7,
    "if_false": 4,
    "nb_actions": 0
}

monkey7 = {
    "starting_items": [72, 51, 93, 63, 80, 86, 81],
    "operation": lambda x: x * x,
    "test": lambda x: x % 11 == 0,
    "if_true": 0,
    "if_false": 4,
    "nb_actions": 0
}

# Define the list of monkeys
monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]


# Define the function to simulate a single turn for a monkey
def simulate_turn(monkey, i_monkey, part):
    # Iterate over each item the monkey is holding
    if (part == 1):
        item_to_remove = []
        for item in monkey["starting_items"]:
            # Update the worry level based on the monkey's operation
            worry_level = monkey["operation"](item)

            # Divide the worry level by three and round down
            worry_level = worry_level // 3
            # Apply the monkey's test to determine where to throw the item
            if monkey["test"](worry_level):
                monkeys[monkey["if_true"]]["starting_items"].append(worry_level)
            else:
                monkeys[monkey["if_false"]]["starting_items"].append(worry_level)
        
            item_to_remove.append(item)
            monkeys[i_monkey]["nb_actions"] += 1

        for it in item_to_remove:
            monkeys[i_monkey]["starting_items"].remove(it)

            # Return the updated worry level and the next monkey
    if (part == 2):
        item_to_remove = []
        for item in monkey["starting_items"]:
            # Update the worry level based on the monkey's operation
            worry_level = monkey["operation"](item)

            # Find the remainder by computing the least commun multiple of the item (worry_level)
            worry_level %= lcm 
            # Apply the monkey's test to determine where to throw the item
            if monkey["test"](worry_level):
                monkeys[monkey["if_true"]]["starting_items"].append(worry_level)
            else:
                monkeys[monkey["if_false"]]["starting_items"].append(worry_level)
        
            item_to_remove.append(item)
            monkeys[i_monkey]["nb_actions"] += 1

        for it in item_to_remove:
            monkeys[i_monkey]["starting_items"].remove(it)

    return

# Define the function to simulate the entire puzzle
def simulate_puzzle(part):

    nb_turn = 1
    # Simulate the puzzle until the worry level reaches 0
    while nb_turn <= MAX_TURN:
        # Simulate a single turn for the current monkey
        for i_monkey, monkey in enumerate(monkeys):
            simulate_turn(monkey, i_monkey, part)

        # Print the current worry level
        nb_turn += 1

# Run the simulation
MAX_TURN = 100
part = 2
simulate_puzzle(part)
list_actions = [nb_actions for nb_actions in map(lambda monkey: monkey["nb_actions"], monkeys)]
result = heapq.nlargest(2, list_actions)[0] * heapq.nlargest(2, list_actions)[1]
if (part == 1): 
    print(f"Part 1 monkey stuff: {result}") 
    
else: print(f"Part 2 monkey stuff: {result}")

