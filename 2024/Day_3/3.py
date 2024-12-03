import re
filename = '3.in'

with open(filename, 'r') as file:
    text = file.read()  # Read the expression from the file

pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(pattern, text)
results = 0

for match in matches:
    match = match[4:-1]
    num1, num2 = match.split(',')
    results += int(num1) * int(num2)

print(f"Résultat partie 1 : {results}")

# ----------------------------------------------------------------

enable_pattern = r"do\(\)"
disable_pattern = r"don't\(\)"
results = 0

enable_matches = list(re.finditer(enable_pattern, text))
disable_matches = list(re.finditer(disable_pattern, text))
matches = []
# def find_valid_zones(enable_matches, disable_matches):
#     valid_zones = []
#     enable_index = 0
#     disable_index = 0

#     while enable_index < len(enable_matches) and disable_index < len(disable_matches):
#         enable_end = enable_matches[enable_index].span()[1]
#         disable_start = disable_matches[disable_index].span()[0]


#         if enable_end < disable_start:
#             valid_zones.append((enable_end, disable_start))
#             enable_index += 1
#         else:
#             disable_index += 1


#     while enable_index < len(enable_matches):
#         enable_end = enable_matches[enable_index].span()[1]
#         valid_zones.append((enable_end, len(text)))
#         enable_index += 1

#     return valid_zones

# def get_mul(text, valid_zones, pattern):
#     results = 0
#     for vals in valid_zones:
#         trimmed_text = text[vals[0] : vals[1]]
#         matches = re.findall(pattern, trimmed_text)

#         for match in matches:
#             match = match[4:-1]
#             num1, num2 = match.split(',')
#             results += int(num1) * int(num2)
#     return results

regex_pattern_2 = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"


for a, b, do, dont in re.findall(regex_pattern_2, text):

    if do or dont:
        enabled = bool(do)
    else:
        x = int(a) * int(b)
        results += x * enabled

print(f"Résultat partie 2 : {results}\n")


