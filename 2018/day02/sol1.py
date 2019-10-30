import sys

filename = sys.argv[1]
file = open(filename, 'r')

threes = 0
twos = 0
for line in file:
    boolThree = False
    boolTwo = False
    line = line.strip()
    d = {}
    for ch in line:
        d[ch] = d[ch] + 1 if d.get(ch) != None else 1
    for key in d:
        if not boolThree and d[key] == 3:
            threes += 1
            boolThree = True
        if not boolTwo and d[key] == 2:
            twos += 1
            boolTwo = True
file.close()
print(threes * twos)
        


