import numpy as np

f = open('Day2.txt' , "r")
lines = f.readlines()
f.close()

matrix = []
for line in lines:
    matrix.append(list(map(int, line.split())))

safe = 0
unsafe = 0


def isSafe(line):
    direction = 1 if (line[1] - line[0]) > 0 else -1
    s = True
    for i in range(1, len(line)):
        if abs(line[i] - line[i - 1]) < 1 or abs(line[i] - line[i - 1]) > 3:
            s = False
            break
        else:            
            if (line[i] - line[i - 1]) > 0 and direction == -1:
                s = False
                break
            elif (line[i] - line[i - 1]) < 0 and direction == 1:
                s = False
                break

    return True if s else False


for line in matrix:
    s = isSafe(line)
    safe += 1 if s else 0
    unsafe += 0 if s else 1

print("safe:" + str(safe))
print("unsafe:" + str(unsafe))

safe = 0
unsafe = 0

for line in matrix:
    subsets = []
    for i in range(len(line)):
        subsets.append(line[:i] + line[i+1:])
    
    s = any(isSafe(subset) for subset in subsets)

    safe += 1 if s else 0
    unsafe += 0 if s else 1

print("safe:" + str(safe))
print("unsafe:" + str(unsafe))