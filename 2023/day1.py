numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("part one: ",sum(int(x) for x in [[x for x in line if x in numbers][0]+[x for x in line if x in numbers][-1] for line in open("dayone.txt", "r").readlines()]))

# Part 2

with open("dayone.txt") as f:
    data = f.readlines()

lines = []
for index, line in enumerate(data):
    line = line.strip().replace("zero", "z0o").replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    stuff = [x for x in line if x in numbers]
    lines.append(stuff[0]+stuff[-1])

print("part two: ",sum(int(x) for x in lines))
