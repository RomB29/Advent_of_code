filename = r'1_2.in'
with open(filename, 'r') as f:
    lines = f.read().strip().split()

string_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

output = 0


def find_combination(word):
    words = []
    for start in range(len(word)):
        for end in range(start + 1, len(word) + 1):
            substring = word[start:end]
            if substring in string_to_int:
                # Perform some action with the matched substring and its numeric value
                print(f"Substring: {substring}, Numeric Value: {string_to_int[substring]}")
                words.append(string_to_int[substring])
    return words
details_array = []
for line in lines:
    temp_array = []
    current_word = ""
    temp = []
    for c in line:
        if c.isdigit():
            temp_array.append(int(c))

        if c.isalpha():
            current_word += c

        if current_word:
            temp = find_combination(current_word)
            if len(temp) != 0:
                temp_array.append(temp[0])
                temp = []
                current_word = current_word[-1]
    details_array.append(temp_array)
    output += (int(str(temp_array[0]) + str(temp_array[-1])))

print(f"The result is: {output}")