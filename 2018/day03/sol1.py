import sys

filename = sys.argv[1]
file = open(filename, 'r')

# Xtreme brute force :)
o = {}
d = {}

for line in file:
    aSplit = line.split("@")
    name = int(aSplit[0][1:])
    aSplit = aSplit[1].split(":")
    xySplit = aSplit[0].split(",")
    distSplit = aSplit[1].split("x")
    x, y = int(xySplit[0]), int(xySplit[1])
    w, h = int(distSplit[0]), int(distSplit[1])
    for i in range(x, x+w):
        for j in range(y, y+h):
            t = (i, j)
            if t in d:
                o[t] = 1
            else:
                d[t] = 1
file.close()

print(len(o))