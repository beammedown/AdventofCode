with open("./input.txt", "r") as f:
    data = f.readlines()

parseddata = []
for line_index, line in enumerate(data):
    parseddata.append([])
    for item_index, item in enumerate(line.strip()):
        parseddata[line_index].append(item)

cursor: list[int] = []
cursor_dir: list[int] = []

for line_index, line in enumerate(data):
    for item_index, item in enumerate(line.strip()):
        if item == "^":
            cursor = [line_index, item_index]
            cursor_dir = [-1, 0]
        elif item == "<":
            cursor = [line_index, item_index]
            cursor_dir = [0, -1]
        elif item == ">":
            cursor = [line_index, item_index]
            cursor_dir = [0, 1]
        elif item == "v":
            cursor = [line_index, item_index]
            cursor_dir = [1, 0]
        else:
            pass

while (cursor[0]+cursor_dir[0] < len(parseddata) and 
       cursor[0]+cursor_dir[0] > -1 and 
       cursor[1]+cursor_dir[1]< len(parseddata[cursor[1]]) and 
       cursor[1]+cursor_dir[1] > -1):
    if parseddata[cursor[0]][cursor[1]] == "#":
        cursor[0] -= cursor_dir[0]
        cursor[1] -= cursor_dir[1]

        # Change 90° to the right
        if cursor_dir == [-1, 0]:
            cursor_dir = [0, 1]
        elif cursor_dir == [1, 0]:
            cursor_dir = [0, -1]
        elif cursor_dir == [0, 1]:
            cursor_dir = [1, 0]
        elif cursor_dir == [0, -1]:
            cursor_dir = [-1, 0]
 
    # Ich muss auch checken ob die neue Position nach einem drehen gut ist
    next_loc = [cursor[0]+cursor_dir[0], cursor[1]+cursor_dir[1]]
    if parseddata[next_loc[0]][next_loc[1]] == "#":
        # Change 90° to the right
        if cursor_dir == [-1, 0]:
            cursor_dir = [0, 1]
        elif cursor_dir == [1, 0]:
            cursor_dir = [0, -1]
        elif cursor_dir == [0, 1]:
            cursor_dir = [1, 0]
        elif cursor_dir == [0, -1]:
            cursor_dir = [-1, 0]
        next_loc = [cursor[0]+cursor_dir[0], cursor[1]+cursor_dir[1]]
    # Set current location X and new set new location
    parseddata[cursor[0]][cursor[1]] = "X"
    cursor = next_loc

total = 0
for line in parseddata:
    for item in line:
        if item == "X":
            total += 1
print(total+1)
