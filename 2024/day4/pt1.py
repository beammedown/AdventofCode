def horizontal_search(data: list[list[str]]) -> int:
    total = 0
    for row in data:
        for index, item in enumerate(row[:-3]):
            if item == 'X' and row[index+1] == 'M' and row[index+2] == 'A' and row[index+3] =='S':
                total += 1
            elif item == 'S' and row[index+1] == 'A' and row[index+2] == 'M' and row[index+3] =='X':
                total += 1
    return total

def vertical_search(data: list[list[str]]) -> int:
    total = 0
    for index, row in enumerate(data[:-3]):
        for rowindex, item in enumerate(row):
            if item == 'X' and data[index+1][rowindex] == 'M' and data[index+2][rowindex] == 'A' and data[index+3][rowindex] =='S':
                total += 1
            elif item == 'S' and data[index+1][rowindex] == 'A' and data[index+2][rowindex] == 'M' and data[index+3][rowindex] =='X':
                total += 1
    return total

def diagonal_search(data: list[list[str]]):
    total = 0

    for index, row in enumerate(data):
        for rowindex, item in enumerate(row):
            if index < len(data)-3 and rowindex < len(row)-3:
                if item == 'X' and data[index+1][rowindex+1] == 'M' and data[index+2][rowindex+2] == 'A' and data[index+3][rowindex+3] =='S':
                   total += 1
                if item == 'S' and data[index+1][rowindex+1] == 'A' and data[index+2][rowindex+2] == 'M' and data[index+3][rowindex+3] =='X':
                   total += 1

            if index < len(data)-3 and rowindex > 2:
                if item == 'X' and data[index+1][rowindex-1] == 'M' and data[index+2][rowindex-2] == 'A' and data[index+3][rowindex-3] == 'S':
                    total += 1
                if item == 'S' and data[index+1][rowindex-1] == 'A' and data[index+2][rowindex-2] == 'M' and data[index+3][rowindex-3] == 'X':
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

print(horizontal_search(data))
print(vertical_search(data))
print(diagonal_search(data))

total = horizontal_search(data) + vertical_search(data) + diagonal_search(data)
print("total: ",total)

