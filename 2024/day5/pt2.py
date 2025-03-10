with open("./input.txt", "r") as f:
    data = f.readlines()


def correctly_ordered(rules: dict[str, list[str]], itemlist: list[str]) -> bool:
    for rule in rules.keys():
        crule = rules[rule]
        try:
            cindex = itemlist.index(rule)
        except:
            continue
        for item in crule:
            try:
                if (itemlist.index(item) < cindex):
                    return False
            except:
                continue
    return True

def rulecheck(rule_key: str, rule_vals: list[str], l: list[str]) -> bool:
    try:
        rule_ind = l.index(rule_key)
    except:
        return True
    for val in rule_vals:
        try:
            if rule_ind > l.index(val):
                return False
        except:
            pass
    return True

rules: dict[str, list[str]] = {}

for item in data:
    if item == '\n':
        break
    if item.strip().split('|')[0] in rules.keys():
        rules[item.strip().split('|')[0]].append(item.strip().split('|')[1])
    else:
        rules[item.strip().split('|')[0]] = [item.strip().split('|')[1]]

ind: int = data.index('\n')
lines: list[str] = [item.strip() for item in data[ind+1:]]

getout: bool = False
total: int = 0
working: list[list[str]] = []

for line in lines:
    linelist = line.split(',')

    getout = correctly_ordered(rules, linelist)

    if not getout:
        working.append(linelist)
        getout = False
    else:
        pass

print(working)

total = 0

for item in working:
    changed_item = item
    while not correctly_ordered(rules, item):
        for rule in rules.keys():
            if not rulecheck(rule, rules[rule], changed_item):
                changed_item.remove(rule)
                changed_item.insert(0, rule)
    total += int(changed_item[len(changed_item)//2])
    print(changed_item)
print(total)
