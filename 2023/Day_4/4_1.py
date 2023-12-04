import re

filename = "4_1.in"
pattern = re.compile(r'Card\s+(\d+):\s*(.+?)\s*\|\s*(.+)')

with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')

data_parsed = {}

for line in lines:

    match = pattern.match(line)

    if match:
        card_number, values1, values2 = match.groups()
        current_card = int(card_number)
        data_parsed[f"Card {current_card}"] = {'Winning numbers': list(map(int, values1.split())), 'My draw numbers': list(map(int, values2.split()))}

def part_1(data):
    winning_headers = "Winning numbers"
    draw_numbers = "My draw numbers"
    res = 0
    for h in data:
        winners = list(set(data[h][winning_headers]).intersection(set(data[h][draw_numbers])))
        if len(winners) > 0:
            res += 2 ** (len(winners) - 1)
    print(f"Résultat part 1: {int(res)}")
    return

#
#     PART 2
#

def win_copies(data, card_number, copies, end):
    winning_headers = "Winning numbers"
    draw_numbers = "My draw numbers"

    # Check if there are matching numbers
    winners = list(set(data[f"Card {card_number}"][winning_headers]).intersection(data[f"Card {card_number}"][draw_numbers]))

    # If there are winners, calculate the number of copies won
    if len(winners) > 0:
        for i in range(1, len(winners) + 1):
            copies[f"Card {card_number + i}"] += 1
            win_copies(data, card_number + i, copies, end)
    else:
        return


def part_2(data):
    copies = {f"Card {i}": 1 for i in range(1, len(data) + 1)}  # Initialize copies dictionary
    # Start winning copies from each card
    end = len(data)
    card_number = 1
    for i in range(len(data)):
        win_copies(data, card_number, copies, end)
        card_number += 1

    total_scratchcards = sum(copies.values())
    print(f"Total Scratchcards: {total_scratchcards}")
    return total_scratchcards

if __name__ == '__main__':
    part_1(data_parsed)
    part_2(data_parsed)