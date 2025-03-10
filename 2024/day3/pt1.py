import re

with open("./day3/input.txt", "r") as f:
    data = f.read()


matches: list[str] = re.findall("mul[(][0-9]*,[0-9]*[)]", data)

total = 0

for item in matches:
    total += int(item.split(",")[0][4:]) * int(item.split(",")[1][:-1])

print(total)