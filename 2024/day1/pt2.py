with open("./day1/input1.txt", "r") as f:
    data = f.readlines()

    data_left = [int(i.split("   ")[0].strip()) for i in data]
    data_right = [int(i.split("   ")[1].strip()) for i in data]


total = 0

occurence_counter = {}

for item in data_left:
    occurence_counter[item] = data_right.count(item)


for item in occurence_counter.keys():
    tmp = item * occurence_counter[item]
    total += tmp

print(total)