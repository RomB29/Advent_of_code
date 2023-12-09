import itertools
from collections import Counter


filename = "7.in"

with open(filename, 'r') as f:
    data = f.read().strip().split('\n')
    data = [d.split() for d in data]
list_hands = [str(h[0]) for h in data]
value_hands = [int(h[1]) for h in data]


hands_ranks = {
    "high": 1, # high
    "pair": 2, # pair
    "two_pairs": 3, # 2 pairs
    "brelan": 4,
    "full": 5,
    "square": 6,
    "ace": 7
}

cards_ranks = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}


def sort_hand(hand, card_ranks):
    out = []
    occurrence = Counter(hand)
    # Sort the cards based on the sorting key
    for occ in occurrence:
        out.append((occurrence[occ], card_ranks[occ]))

    sorted_values = sorted(out, key=lambda x: x[0], reverse=True)

    return sorted_values

def get_combination(list_hands, card_ranks):
    all_combinations = []

    for i_hand, hand in enumerate(list_hands):
        ranked_combinations = sort_hand(hand, card_ranks)
        all_combinations.append([(hand, value_hands[i_hand]), ranked_combinations])

    return all_combinations

def refinement_sort_hands(hands_first_sort):


    sorted_hands = sorted(hands_first_sort, key=lambda hand: hand[1], reverse=False)

    return sorted_hands

list_combination = get_combination(list_hands, cards_ranks)
hands_sorted = refinement_sort_hands(list_combination)


results = sum([(i + 1) * val[0][1] for i, val in enumerate(hands_sorted)])




print(results)