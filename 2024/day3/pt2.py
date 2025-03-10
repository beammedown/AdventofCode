from icecream import ic
import re

with open("./day3/input.txt", "r") as f:
    data = f.read()


matches: list[tuple[str]] = re.findall("(mul[(][0-9]*,[0-9]*[)])|(do[()]{2})|(don[']t[()]{2})", data)

total = 0
doit = True

for item in matches:
    if item[1] != '':
        doit = True
        continue
    elif item[2] != '':
        doit = False
        continue
    
    if item[0] != '' and doit:
        total += int(item[0].split(",")[0][4:]) * int(item[0].split(",")[1][:-1])

print(total)