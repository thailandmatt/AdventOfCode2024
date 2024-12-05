f = open('Day5.txt' , "r")
lines = f.readlines()
f.close()

map = {}
sections = []

inSections = False
for i in range(len(lines)):
    lines[i] = lines[i].strip()    
    if lines[i] == '':
        inSections = True
    elif inSections:
        sections.append(lines[i])
    else:
        split = lines[i].split('|')
        if split[0] not in map:
            map[split[0]] = []
        map[split[0]].append(split[1])

result = 0
incorrectSections = []

for section in sections:
    split = section.split(',')
    ok = True
    for i in range(len(split) - 1):        
        for j in range(i + 1, len(split)):
            if (split[i] not in map or split[j] not in map[split[i]]):
                ok = False
                break
    if ok:
        result += int(split[len(split)//2])
    else:
        incorrectSections.append(section)

print(result)

result2 = 0

for key in map:
    map[key].append(key)

for section in incorrectSections:
    split = section.split(',')
    newSplit = []

    while (len(split) > 1):        
        for i in range(len(split)):        
            ok = True
            for j in range(i, len(split)):
                if (split[i] not in map or split[j] not in map[split[i]]):
                    ok = False
                    break
            if ok:
                newSplit.append(split[i])
                del split[i]
                break
    
    newSplit.append(split[0])

    result2 += int(newSplit[len(newSplit)//2])

print(result2)