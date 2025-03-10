with open("daythree.txt") as f:
    data = f.readlines()
    
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
found = set()
for line in data:
    for char in line:
        if char != '.' and char not in nums and char != '\n':
            found.add(char)
            

summe = 0

for lindex, line in enumerate(data):
    line = line.strip()
    num = 0
    counts = False
    
    for cindex, char in enumerate(line):
        if char in nums:
            if num == 0:
                num += int(char)
            else:
                num = (num*10)+int(char)

            try:
                if data[lindex][cindex+1] in found:
                    counts = True
            except:
                pass
            try:
                if data[lindex][cindex-1] in found:
                    counts = True
            except:
                pass
            try:
                if data[lindex+1][cindex] in found:
                    counts = True
            except:
                pass
            
            try:
                if data[lindex+1][cindex+1] in found:
                    counts = True
            except:
                pass
            
            try:
                if data[lindex+1][cindex-1] in found:
                    counts = True
            except:
                pass
            
                
            try:
                if data[lindex-1][cindex] in found:
                    counts = True
            except:
                pass
            try:
                if data[lindex-1][cindex+1] in found:
                    counts = True
            except:
                pass
            try:
                if data[lindex-1][cindex-1] in found:
                    counts = True
            except:
                pass
        else:
            if num != 0 and counts:
                summe += num

            counts = False
            num = 0
    if num != 0 and counts:
        summe += num

    counts = False
    num = 0

        
print(summe)