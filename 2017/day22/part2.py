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
            infected[(x,y)] = "I"
        x += 1
    y -= 1

# returns new facing
def turn(facing, direction):
    leftDict = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
    }
    rightDict = {
        "N": "E",
        "W": "N",
        "S": "W",
        "E": "S"
    }
    reverseDict = {
        "N": "S",
        "S": "N",
        "W": "E",
        "E": "W"
    }
    if direction == "left":
        return leftDict[facing]
    elif direction == "right":
        return rightDict[facing]
    else:
        return reverseDict[facing]

def move(facing, location):
    if facing == "N":
        return (location[0], location[1]+1)
    elif facing == "E":
        return (location[0]+1, location[1])
    elif facing == "S":
        return (location[0], location[1]-1)
    elif facing == "W":
        return (location[0]-1, location[1])

virusLoc = (0, 0)
facing = "N"
infections = 0
for times in range(10000000):
    #if times % 10000 == 0:
        #print(times, virusLoc)
    if virusLoc in infected:
        vType = infected[virusLoc]
        if vType == "W":
            infections += 1
            infected[virusLoc] = "I"
        elif vType == "I":
            facing = turn(facing, "right")
            infected[virusLoc] = "F"
        elif vType == "F":
            facing = turn(facing, "reverse")
            del infected[virusLoc]
    else:
        facing = turn(facing, "left")
        infected[virusLoc] = "W"

    virusLoc = move(facing, virusLoc)

print(infections)
