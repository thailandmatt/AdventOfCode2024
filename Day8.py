import itertools


f = open('Day8.txt' , "r")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

antennas = {}

for row in range(len(lines)):
    for col in range(len(lines[row])):
        char = lines[row][col]
        if char != '.':
            if char not in antennas:
                antennas[char] = []
            
            antennas[char].append((row, col))

antinodes = {}

for antenna in antennas:
    for pair in itertools.combinations(antennas[antenna], 2):
        diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
        a1 = (pair[0][0] - diff[0], pair[0][1] - diff[1])
        a2 = (pair[1][0] + diff[0], pair[1][1] + diff[1])

        if (a1[0] >= 0 and a1[1] >= 0 and a1[0] < len(lines) and a1[1] < len(lines[0])):
            if a1 not in antinodes: antinodes[a1] = True

        if (a2[0] >= 0 and a2[1] >= 0 and a2[0] < len(lines) and a2[1] < len(lines[0])):
            if a2 not in antinodes: antinodes[a2] = True

print(len(antinodes))

antinodes2 = {}

for antenna in antennas:
    for pos in antennas[antenna]:
        if pos not in antinodes2: antinodes2[pos] = True

for antenna in antennas:
    for pair in itertools.combinations(antennas[antenna], 2):
        diff = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])

        cur = (pair[0][0] - diff[0], pair[0][1] - diff[1])
        while (cur[0] >= 0 and cur[1] >= 0 and cur[0] < len(lines) and cur[1] < len(lines[0])):
            if cur not in antinodes2: antinodes2[cur] = True
            cur = (cur[0] - diff[0], cur[1] - diff[1])

        cur = (pair[1][0] + diff[0], pair[1][1] + diff[1])
        while (cur[0] >= 0 and cur[1] >= 0 and cur[0] < len(lines) and cur[1] < len(lines[0])):
            if cur not in antinodes2: antinodes2[cur] = True
            cur = (cur[0] + diff[0], cur[1] + diff[1])

print(len(antinodes2))