
def parser_data(filename: str) -> dict:
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n\n')
    # Initialize an empty dictionary to store the parsed data
    parsed_data = {}

    for section in data:
        # Split each section into lines
        line = section.split('\n')
        section_name = line[0].split(':')[0].strip()
        if section_name == 'seeds':
            parsed_data[section_name] = list(map(int, line[0].split(':')[1].split()))
        else:
            parsed_data[section_name] = [tuple(map(int, l.split())) for l in line[1:]]
    return parsed_data



if __name__ == '__main__':
    filename = "5.in"
    data = parser_data(filename)
    seed_header = list(data.keys())[0]
    others_headers = list(data.keys())[1:]

    seed_numbers = len(data["seeds"])
    for h in others_headers:
        new = []
        for seed in data[seed_header]:
            for (dest, src, step) in data[h]:
                if src <= seed <= src + step:
                    new.append(seed - src + dest)
                    break
            else:
                new.append(seed)
        data[seed_header] = new

    print(f"Résultat part 1: {min(data[seed_header])}")