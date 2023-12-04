

filename = "3_1.in"

with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')


number_ranges = []
width_sequences = len(lines[0])
height_sequences = len(lines)

special_characters = "'!@#$%^&*()-+?_=,<>/"


def is_valid_number(start_row, start_col, end_col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for col in range(start_col, end_col + 1):

        for dr, dc in directions:
            nr, nc = start_row + dr, col + dc
            if 0 <= nr < width_sequences and 0 <= nc < height_sequences:
                if lines[nr][nc] in special_characters:
                    return True, (nr, nc)

    return False, None

def get_value(start_row, start_col, end_col):
    return (int(lines[start_row][start_col : end_col + 1]))

def result_part_1(list_positions):

    res = 0
    for row in list_positions:
        res += get_value(row[0][0], row[0][1], row[1][1])

    print(f"Result part 1: {res}")
    return

def find_similar_numbers(number_ranges): # Part 2
    special_char_dict = {}

    for start, end, special_char_location in number_ranges:
        if special_char_location not in special_char_dict:
            special_char_dict[special_char_location] = []

        number = int(lines[start[0]][start[1]: end[1] + 1])
        special_char_dict[special_char_location].append(number)

    return special_char_dict


def result_part_2(number_ranges): # Part 2
    final_result = 0
    similar_numbers_dict = find_similar_numbers(number_ranges)
    for header in similar_numbers_dict:
        if len(similar_numbers_dict[header]) > 1:
            unit_result = 1
            for val in similar_numbers_dict[header]:
                unit_result *= val
            final_result += unit_result
    print(f"Result part 2: {final_result}")

    return
def process_number(row, start_col, col, deduction):
    end_col = col - 1 + deduction
    is_valid, special_char_location = is_valid_number(row, start_col, end_col)

    if is_valid:
        number_ranges.append(((row, start_col), (row, end_col), (special_char_location)))

def is_valid_special_character(row, col, frame_width):
    return 0 <= col + 1 < frame_width and lines[row][col + 1].isdigit()


for row in range(height_sequences):
    number = ""
    start_col = None
    deduction = 0
    for col in range(width_sequences):
        current_char = lines[row][col]
        if current_char.isdigit() and (current_char not in special_characters):
            if start_col is None:
                start_col = col
            number += current_char

        if current_char in special_characters and lines[row][col - 1].isdigit():
            deduction -= 1

        if current_char in special_characters and lines[row][col + 1].isdigit():
            deduction = 0

        if current_char in special_characters and lines[row][col - 1].isdigit() and lines[row][col + 1].isdigit():
            process_number(row, start_col, col, deduction)
            number = ""
            start_col = None

        if current_char == '.' and number != "" and current_char:
            process_number(row, start_col, col, deduction)
            number = ""
            start_col = None

        if current_char == '.':
            start_col = None
            deduction = 0

        if number != "" and col == width_sequences - 1:
            process_number(row, start_col, col + 1, deduction)
            number = ""
            start_col = None

# Print the result
for start, end, not_use in number_ranges:
    print(f"Number: {lines[start[0]][start[1] : end[1] + 1]}, Start: ({start[0]}, {start[1]}), End: ({end[0]}, {end[1]})")
result_part_1(number_ranges)
result_part_2(number_ranges)

