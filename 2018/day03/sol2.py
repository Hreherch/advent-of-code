import sys

filename = sys.argv[1]
file = open(filename, 'r')

# X-treme Brute Force :)
squares = []
d = {}

for line in file:
    aSplit = line.split("@")
    name = int(aSplit[0][1:])
    aSplit = aSplit[1].split(":")
    xySplit = aSplit[0].split(",")
    distSplit = aSplit[1].split("x")
    x, y = int(xySplit[0]), int(xySplit[1])
    w, h = int(distSplit[0]), int(distSplit[1])
    # keep track of squares for round 2
    squares.append((name, x, y, w, h))
    # might as well build the dict while we're here
    for i in range(x, x+w):
        for j in range(y, y+h):
            t = (i, j)
            d[t] = d[t] + 1 if t in d else 1
file.close()

for square in squares:
    thisSquare = True
    x = square[1]
    y = square[2]
    w = square[3]
    h = square[4]
    for i in range(x, x+w):
        for j in range(y, y+h):
            t = (i, j)
            if d[t] > 1:
                thisSquare = False
            if not thisSquare: break
        if not thisSquare: break
    if thisSquare: print(square[0])