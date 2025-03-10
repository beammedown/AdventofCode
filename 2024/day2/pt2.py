def is_safe(report: list[int]) -> bool:
    differences = [report[i+1]-report[i] for i in range(len(report)-1)]

    increasing = differences[0] > 0
    for item in differences:
        if (item > 0) == increasing and (item != 0) and (item >= -3) and (item <= 3):
            safe = True
        else:
            safe = False
            break
    return safe


with open("./day2/input.txt", "r") as f:
    data = f.readlines()

count_safe_reports = 0

increasing = True


for line in data:
    report = [int(num.strip()) for num in line.split()]

    if is_safe(report):
        count_safe_reports += 1
    else:
        for indice in range(len(report)):
            new_report = report.copy()
            new_report.pop(indice)

            if is_safe(new_report):
                count_safe_reports += 1
                break
        

print(count_safe_reports)