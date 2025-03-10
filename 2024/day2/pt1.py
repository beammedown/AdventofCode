with open("./day2/input.txt", "r") as f:
    data = f.readlines()

count_safe_reports = 0
safe = False
for line in data:
    report = [int(i) for i in line.strip().split(" ")]
    differences = [report[i+1]-report[i] for i in range(len(report)-1)]

    increasing = differences[0] > 0
    for item in differences:
        if (item > 0) == increasing and (item != 0) and (item >= -3) and (item <= 3):
            safe = True
        else:
            safe = False
            break
    if safe:
        count_safe_reports += 1


print(count_safe_reports)