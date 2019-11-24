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

best = (1, 3)
bigP = -100000
for x in range(1, 299):
    for y in range(3, 301):
        p = grid[(x, y)] + grid[(x+1, y)] + grid[(x+2, y)] +\
            grid[(x, y-1)] + grid[(x+1, y-1)] + grid[(x+2, y-1)] +\
            grid[(x, y-2)] + grid[(x+1, y-2)] + grid[(x+2, y-2)]
        if p > bigP:
            bigP = p
            best = (x, y-2)
              
print(best)
 