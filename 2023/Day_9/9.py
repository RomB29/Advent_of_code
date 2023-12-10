filename = "9.in"

with open(filename, 'r') as f:
    data_parsed = [list(map(int, line.split(' '))) for line in f]


def difference_counter(liste: list) -> list:
    new_row = [v - liste[i - 1] for i, v in enumerate(liste) if i > 0]
    return new_row


def compute(liste: list) -> list:
    output = [liste]
    output.append(difference_counter(liste))

    while output[-1] != [0 for _ in range(len(output[-1]))]:
        output.append(difference_counter(output[-1]))

    return output

def extrapolation_part_1(liste: list) -> list:
    new_liste = list(reversed(liste))
    new_liste[0].append(0)
    for i_l, l in enumerate(new_liste[1:]):
       extrapo = l[-1] + new_liste[i_l][-1]
       new_liste[i_l + 1].append(extrapo)

    output = new_liste[i_l + 1][-1]
    return output

def extrapolate_backward(liste: list) -> list:
    new_liste = list(reversed(liste))
    new_liste[0].insert(0, 0)
    for i_l, l in enumerate(new_liste[1:]):
        extrapo = l[0] - new_liste[i_l][0]
        new_liste[i_l + 1].insert(0, extrapo)

    output = new_liste[i_l + 1][0]
    return output

if __name__ == '__main__':
    part_1 = 0
    part_2 = 0
    for l in data_parsed:
        unit_compute = compute(l)
        part_1 += extrapolation_part_1(unit_compute)
        part_2 += extrapolate_backward(unit_compute)

    print(f"Résultat part 1: {part_1}")
    print(f"Résultat part 2: {part_2}")