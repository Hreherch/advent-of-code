import sys

filename = sys.argv[1]
file = open(filename, 'r')

grid = []
for line in file:
    row = []
    for ch in line.strip():
        row.append(ch)
    grid.append(row)

infected = {}
y = len(grid)//2
for row in grid:
    x = -(len(grid)//2)
    for elem in row:
        if elem == "#":
            infected[(x,y)] = True
        x += 1
    y -= 1

# returns virusLoc, facing
def getNextLoc(currentLoc, facing, currentNodeWasInfected):
    if facing == "N":
        if currentNodeWasInfected:
            return (currentLoc[0]+1, currentLoc[1]), "E"
        else:
            return (currentLoc[0]-1, currentLoc[1]), "W"
    elif facing == "E":
        if currentNodeWasInfected:
            return (currentLoc[0], currentLoc[1]-1), "S"
        else:
            return (currentLoc[0], currentLoc[1]+1), "N"
    elif facing == "S":
        if currentNodeWasInfected:
            return (currentLoc[0]-1, currentLoc[1]), "W"
        else:
            return (currentLoc[0]+1, currentLoc[1]), "E"
    elif facing == "W":
        if currentNodeWasInfected:
            return (currentLoc[0], currentLoc[1]+1), "N"
        else:
            return (currentLoc[0], currentLoc[1]-1), "S"

virusLoc = (0, 0)
facing = "N"
infections = 0

for times in range(10000):
    wasInfected = virusLoc in infected
    
    if wasInfected:
        del infected[virusLoc]
    else:
        infected[virusLoc] = True
        infections += 1
    
    virusLoc, facing = getNextLoc(virusLoc, facing, wasInfected)

print(infections)
