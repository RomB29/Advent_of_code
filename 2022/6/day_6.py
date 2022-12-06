filename   = "input.in"
taille_fen = 4 # 14 for the second part of the puzzle
i          = 0
result     = 0

def read_file(filename):
    with open(filename) as f:
    # Parsing the data
        datas = f.read()
    return datas

def has_dups(l): 
    return len(set(l)) < len(l)

datas = read_file(filename)

while i < len(datas) - taille_fen:

    if not(has_dups(datas[i : i + taille_fen])):
        result = i + taille_fen
        break
    i += 1

print(f"First marker after character {result}")

