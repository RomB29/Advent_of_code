filename = '4.in'

with open(filename, 'r') as file:
    text = file.read().splitlines()  # Read the expression from the file

result_first_part = 0
for r in range(len(text)):
    for c in range(len(text[0])):
        if text[r][c] != "X":
            continue
        for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            if not(0 <= r + 3 * dr < len(text) and 0 <= c + 3 * dc < len(text[0])): #check limit
                continue
            if text[r + dr][c + dc] == "M" and text[r + 2 * dr][c + 2 * dc] == "A" and text[r + 3 * dr][c + 3 * dc] == "S":
                result_first_part += 1

print(f"Résultat partie 1: {result_first_part}")


result_second_part = 0
for r in range(1, len(text) - 1):
    for c in range(1, len(text[0]) - 1):
        if text[r][c] != "A":
            continue
        corners = text[r - 1][c - 1], text[r - 1][c + 1], text[r + 1][c + 1], text[r + 1][c - 1]
        pattern = "".join(corners)
        if pattern in ["SMMS", "MSSM", "SSMM", "MMSS"]:
            result_second_part += 1

print(f"Résultat partie 2: {result_second_part}")