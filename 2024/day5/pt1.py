with open("./input.txt", "r") as f:
    data = f.readlines()


rules: dict[str, list[str]] = {}

for item in data:
    if item == '\n':
        break
    if item.strip().split('|')[0] in rules.keys():
        rules[item.strip().split('|')[0]].append(item.strip().split('|')[1])
    else:
        rules[item.strip().split('|')[0]] = [item.strip().split('|')[1]]

ind = data.index('\n')
lines = [item.strip() for item in data[ind+1:]]

getout = False
total = 0
working = []

for line in lines:
    linelist = line.split(',')
    for rule in rules.keys():
        if getout:
            break
        crule = rules[rule]
        try:
            cindex = linelist.index(rule)
        except:
            continue
        for item in crule:
            try:
                counterpart = linelist.index(item)
                if (linelist.index(item) < cindex):
                    getout = True
            except:
                continue

    if not getout:
        working.append(linelist)
    else:
        getout = False

total = 0

for item in working:
    middle_index = len(item) // 2
    num = int(item[middle_index])
    total += num

print(total)
