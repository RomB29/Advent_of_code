import re
from functools import reduce

filename = "2_1.in"

dict_data = {}
criterias = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')

def check_feasibility(data, criterias):
    if data[1] in criterias:
        result = criterias[data[1]] < data[0]
        return result # pass (True) or fail (False)
    return


## Parsing the data
for l in lines:
    header = l.split(":")[0]
    data = l.split(":")[1].strip()
    data_splitted = [game.strip() for game in data.split(';')]
    game_result = []
    for split in data_splitted:
        tuples = [(int(quantity), color.strip()) for quantity, color in (ball.strip().split() for ball in split.split(','))]
        game_result.append(tuples)
    dict_data[header] = game_result


def part_1(dict_data: dict) -> None:
    ## compute the data -- Part 1
    output = []
    for h in dict_data:
        impossible = False
        current_game = int(re.search(r'\d+', h).group())
        for split in dict_data[h]:
            for nb_colors in split:
                res = check_feasibility(nb_colors, criterias)
                if not res:
                    output.append(current_game)
                else:
                    output = [game for game in output if game != current_game]
                    impossible = True
                    break
            if impossible:
                break
    output = set(output)
    print(f"Result part 1: {sum(output)}")

def part_2(dict_data: dict) -> None:
    ## compute the data -- Part 2
    output = []
    for h in dict_data:
        current_game = int(re.search(r'\d+', h).group())
        temp_dict = {"red": -1, "green": -1, "blue": -1}
        for split in dict_data[h]:
            for nb_colors in split:
                if nb_colors[1] in temp_dict:
                    if nb_colors[0] > temp_dict[nb_colors[1]]:
                        temp_dict[nb_colors[1]] = nb_colors[0]
        output.append(reduce(lambda x, y: x * y, [temp_dict[color] for color in temp_dict]))
    result = sum(output)
    print(f"Result part 2: {result}")

if __name__ == "__main__":
    part_1(dict_data)
    part_2(dict_data)


