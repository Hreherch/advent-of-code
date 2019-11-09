import sys

gridSerialNumber = int(sys.argv[1])

grid = {}
for x in range(1, 301):
    rackId = x + 10
    for y in range(1, 301):
        powerLevel = (y * rackId) + gridSerialNumber
        powerLevel *= rackId
        if powerLevel > 100:
            s = str(powerLevel)
            powerLevel = int(s[-3])
        else:
            powerLevel = 0
        powerLevel -= 5
        grid[(x,y)] = powerLevel

# ugh this is slow
best = (1, 1, 1)
bigP = -100000
for x in range(1, 301):
    for y in range(1, 301):
        c = (x, y)
        p = grid[(x, y)]
        for n in range(2, 301):
            # the maximum diagonal point should be in the grid else we can stop checking
            if (c[0]+n, c[1]-n) not in grid:
                break
            c = (c[0]+1, c[1]) # move our reference point to come back when n+=1
            pos = (c[0], c[1]) # this reference point is the first item we take
            p += grid[c]
            for i in range(n-1):
                pos = (pos[0], pos[1]-1)
                p += grid[pos]
            for i in range(n-1):
                pos = (pos[0]-1, pos[1])
                p += grid[pos]
            if p > bigP:
                bigP = p
                best = (x, y-(n-1), n)
                print("candidate", best, p)

print(best)
 