f = open('Day6.txt' , "r")
lines = f.readlines()
f.close()

visits = {}

row = 0
col = 0

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    line = lines[i]
    if '^' in line:
        row = lines.index(line)
        col = line.index('^')

part2Lines = lines.copy()   
startrow = row
startcol = col

while True:
    if (row, col) not in visits:
        visits[(row, col)] = []

    if (lines[row][col] in visits[(row, col)]):
        # been here before
        break

    visits[(row, col)].append(lines[row][col])

    rowDir = 0
    colDir = 0
    curDir = lines[row][col]

    if curDir == '^':
        rowDir = -1
    elif curDir == '>':
        colDir = 1
    elif curDir == 'v':
        rowDir = 1
    elif curDir == '<':
        colDir = -1

    nextDir = curDir
    if curDir == '^':
        nextDir = '>'
    elif curDir == '>':
        nextDir= 'v'
    elif curDir == 'v':
        nextDir = '<'
    elif curDir == '<':
        nextDir = '^'

    if row + rowDir < 0 or row + rowDir >= len(lines) or col + colDir < 0 or col + colDir >= len(lines[row]):
        # end of line
        break

    if (lines[row + rowDir][col + colDir] == '#'):
        # rotate
        rowDir = 0
        colDir = 0
        curDir = nextDir
    
    lines[row] = lines[row][:col] + '.' + lines[row][col + 1:]
    lines[row + rowDir] = lines[row + rowDir][:col + colDir] + curDir + lines[row + rowDir][col + colDir + 1:]        
    row += rowDir
    col += colDir

print(len(visits))  

part2Answer = []
part2Tested = {}

i = 0

for visit in visits:
    for add in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:        
        obRow = visit[0] + add[0]
        obCol = visit[1] + add[1]
        if obRow < 0 or obRow >= len(part2Lines) or obCol < 0 or obCol >= len(part2Lines[obRow]):
            continue

        if ((obRow, obCol) in part2Tested):
            continue

        part2Tested[(obRow, obCol)] = True

        i = i + 1
        if (i % 1000 == 0):
            print(i)

        lines = part2Lines.copy()
        row = startrow
        col = startcol
        if (lines[obRow][obCol] == '.'):
            lines[obRow] = lines[obRow][:obCol] + 'O' + lines[obRow][obCol + 1:]

        visits = {}
        while True:
            if (row, col) not in visits:
                visits[(row, col)] = []

            if (lines[row][col] in visits[(row, col)]):
                # been here before
                part2Answer.append((obRow, obCol))
                break

            visits[(row, col)].append(lines[row][col])

            rowDir = 0
            colDir = 0
            curDir = lines[row][col]

            if curDir == '^':
                rowDir = -1
            elif curDir == '>':
                colDir = 1
            elif curDir == 'v':
                rowDir = 1
            elif curDir == '<':
                colDir = -1

            nextDir = curDir
            if curDir == '^':
                nextDir = '>'
            elif curDir == '>':
                nextDir= 'v'
            elif curDir == 'v':
                nextDir = '<'
            elif curDir == '<':
                nextDir = '^'

            if row + rowDir < 0 or row + rowDir >= len(lines) or col + colDir < 0 or col + colDir >= len(lines[row]):
                # end of line
                break

            if (lines[row + rowDir][col + colDir] == '#' or lines[row + rowDir][col + colDir] == 'O'):
                # rotate
                rowDir = 0
                colDir = 0
                curDir = nextDir
            
            lines[row] = lines[row][:col] + '.' + lines[row][col + 1:]
            lines[row + rowDir] = lines[row + rowDir][:col + colDir] + curDir + lines[row + rowDir][col + colDir + 1:]        
            row += rowDir
            col += colDir
    
print(len(part2Answer))