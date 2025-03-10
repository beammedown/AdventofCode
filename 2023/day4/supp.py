with open("input.txt") as f:
    data = f.readlines()


weights = [1 for x in range(len(data))]

for index, line in enumerate(data):
    line = line.strip()
    splitted = line.split(":")[1].split("|")
    winnings = splitted[0].split(" ")
    customs = splitted[1].split(" ")
    
    while '' in winnings:
        winnings.remove('')
    while '' in customs:
        customs.remove('')
        
    
    counter = 0
    
    for item in customs:
        if item in winnings:
            counter += 1

    for i in range(1, counter+1):
        if index+i >= len(weights):
            continue
        weights[index+i] += weights[index]
        
print(weights)

print(sum(weights))