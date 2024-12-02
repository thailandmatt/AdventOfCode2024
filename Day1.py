f = open('Day1.txt' , "r")
lines = f.readlines()
f.close()

a = []
b = []
for line in lines: 
    x,y = line.split()
    a.append(x)
    b.append(y) 

a.sort()
b.sort()

diff = 0

for i in range(len(a)):        
    diff += abs(int(a[i]) - int(b[i]))

print("diff:" + str(diff))

b_map = {}

for x in b:    
    b_map[x] = b_map[x] + 1 if x in b_map else 1

similar = 0

for y in a:
    similar += (int(y) * (b_map[y] if y in b_map else 0))

print("similar:" + str(similar))