def search(data):
    total = 0
    for linenumber, line in enumerate(data):
        for index, item in enumerate(line):
            if linenumber < len(data)-2 and index < len(line)-2:
                if item == 'M' and data[linenumber+1][index+1] == 'A' and data[linenumber+2][index+2] == 'S':
                    if data[linenumber][index+2] == 'M' and data[linenumber+2][index] == 'S':
                        print("encountered1: ", linenumber, index)
                        total += 1
                    elif data[linenumber][index+2] == 'S' and data[linenumber+2][index] == 'M':
                        print("encountered2: ", linenumber, index)
                        total += 1
                if item == 'S' and data[linenumber+1][index+1] == 'A' and data[linenumber+2][index+2] == 'M':
                    if data[linenumber][index+2] == 'M' and data[linenumber+2][index] == 'S':
                        print("encountered3: ", linenumber, index)
                        total += 1
                    elif data[linenumber][index+2] == 'S' and data[linenumber+2][index] == 'M':
                        print("encountered4: ", linenumber, index)
                        total += 1

    return total

with open("./input.txt", "r") as f:
    raw_data = f.readlines()

data = [[]]
for index, row in enumerate(raw_data):
    for item in row.strip():
        data[index].append(item)
    data.append([])
data.pop()

print(search(data))
