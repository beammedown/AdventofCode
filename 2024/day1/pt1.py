with open("./day1/input1.txt", "r") as f:
    data = f.readlines()

    data_left = [int(i.split("   ")[0].strip()) for i in data]
    data_right = [int(i.split("   ")[1].strip()) for i in data]


total = 0

while len(data_left) > 0:

    min_lef = min(data_left)
    min_right = min(data_right)

    total += abs(min_lef - min_right)

    data_left.remove(min_lef)
    data_right.remove(min_right)

print(total)