import re

f = open('Day3.txt' , "r")
line = f.readlines()[0]
f.close()

result = 0

for i in range(len(line)):
    if line[i:i+4] == 'mul(':
        sub = line[i+4:]
        sub = sub[:sub.index(')')]
        split = sub.split(',')
        if str.isdigit(split[0]) and str.isdigit(split[1]):
            result += int(split[0]) * int(split[1])

print(result)


result = 0
enabled = True

for i in range(len(line)):
    if line[i:i+4] == 'mul(' and enabled:
        sub = line[i+4:]
        sub = sub[:sub.index(')')]
        split = sub.split(',')
        if str.isdigit(split[0]) and str.isdigit(split[1]):
            result += int(split[0]) * int(split[1])
    elif line[i:i+4] == "do()": enabled = True
    elif line[i:i+7] == "don't()": enabled = False

print(result)