# To check if loops infinite -> passes the startpoint with same dir
with open("./input.txt", "r") as f:
    data = f.readlines()

parseddata: list[list[str]] = []
for line_index, line in enumerate(data):
    parseddata.append([])
    for item_index, item in enumerate(line.strip()):
        parseddata[line_index].append(item)

CURSOR_START: list[int] = []
CURSOR_DIR_START: list[int] = []

for line_index, line in enumerate(data):
    for item_index, item in enumerate(line.strip()):
        if item == "^":
            CURSOR_START = [line_index, item_index]
            CURSOR_DIR_START = [-1, 0]
        elif item == "<":
            CURSOR_START = [line_index, item_index]
            CURSOR_DIR_START = [0, -1]
        elif item == ">":
            CURSOR_START = [line_index, item_index]
            CURSOR_DIR_START = [0, 1]
        elif item == "v":
            CURSOR_START = [line_index, item_index]
            CURSOR_DIR_START = [1, 0]
        else:
            pass

def is_infinite(parseddata: list[list[str]], cursor: list[int], cursor_dir:list[int]) -> bool:
    breakout = 0
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


        if cursor == CURSOR_START and cursor_dir == CURSOR_DIR_START:
            return True
 
        if breakout == len(parsed_d)*len(parsed_d[0]):
            return True
        breakout += 1

    return False

total = 0

parsed_d: list[list[str]] = parseddata
for line_i,line in enumerate(parseddata):
    for item_i,item in enumerate(parseddata):
        if parseddata[line_i][item_i] == "#" or ([line_i, item_i] == CURSOR_START):
            continue
        parsed_d[line_i][item_i] = "#"
        if is_infinite(parsed_d, CURSOR_START, CURSOR_DIR_START):
            total += 1
        parsed_d[line_i][item_i] = "."
print(total)
