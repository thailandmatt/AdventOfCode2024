f = open('Day4.txt' , "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

result = 0

def search(row, col, rowDir, colDir, letter, lines):
    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[0]):
        return 0
    if lines[row][col] == letter:
        if letter == 'X':
            total = 0
            total += search(row + 1, col, 1, 0, 'M', lines)
            total += search(row - 1, col, -1, 0, 'M', lines)
            total += search(row + 1, col - 1, 1, -1, 'M', lines)
            total += search(row - 1, col + 1, -1, 1, 'M', lines)
            total += search(row + 1, col + 1, 1, 1, 'M', lines)
            total += search(row - 1, col - 1, -1, -1, 'M', lines)
            total += search(row, col + 1, 0, 1, 'M', lines)
            total += search(row, col - 1, 0, -1, 'M', lines)
            return total
        elif letter == 'M':
            return search(row + rowDir, col + colDir, rowDir, colDir, 'A', lines)
        elif letter == 'A':
            return search(row + rowDir, col + colDir, rowDir, colDir, 'S', lines)
        elif letter == 'S':
            return 1        
    return 0            

for col in range(len(lines[0])):
    for row in range(len(lines)):
        result += search(row, col, 0, 0, 'X', lines)

part2result = 0

for col in range(1, len(lines[0]) - 1):
    for row in range(1, len(lines) - 1):
        if (lines[row][col] == 'A'):
            if (lines[row - 1][col - 1] == 'M' and lines[row + 1][col + 1] == 'S') and (lines[row - 1][col + 1] == 'M' and lines[row + 1][col - 1] == 'S'):
                part2result += 1
            if (lines[row - 1][col - 1] == 'M' and lines[row + 1][col + 1] == 'S') and (lines[row + 1][col - 1] == 'M' and lines[row - 1][col + 1] == 'S'):
                part2result += 1
            if (lines[row - 1][col - 1] == 'S' and lines[row + 1][col + 1] == 'M') and (lines[row - 1][col + 1] == 'S' and lines[row + 1][col - 1] == 'M'):
                part2result += 1
            if (lines[row - 1][col - 1] == 'S' and lines[row + 1][col + 1] == 'M') and (lines[row + 1][col - 1] == 'S' and lines[row - 1][col + 1] == 'M'):
                part2result += 1

print(result)
print(part2result)
