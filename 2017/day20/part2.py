import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

aDict = {}
vDict = {}
pDict = {}

particleId = 0
for line in file:
    match = re.match("p=<(.*)>, v=<(.*)>, a=<(.*)>", line)
    dicts = [pDict, vDict, aDict]
    groups = [match.group(1), match.group(2), match.group(3)]

    for i in range(len(groups)):
        group = groups[i]
        d = dicts[i]
        d[particleId] = []
        for item in group.split(","):
            d[particleId].append(int(item))

    particleId += 1

def updateValues(pDict, vDict, aDict):
    for key in aDict:
        for i in range(3):
            vDict[key][i] += aDict[key][i]
        for i in range(3):
            pDict[key][i] += vDict[key][i]

def collide(pDict, vDict, aDict):
    collisions = 0
    positions = {}
    deletions = {}

    for key in pDict:
        vector = pDict[key]
        vector = (vector[0], vector[1], vector[2])
        if vector in positions:
            positions[vector] += [key]
        else:
            positions[vector] = [key]

    for key in positions:
        if len(positions[key]) > 1:
            for pid in positions[key]:
                deletions[pid] = True

    for key in deletions:
        collisions += 1
        del pDict[key]
        del vDict[key]
        del aDict[key]

    return collisions

ticks = 10000
currentTick = 0

while currentTick < ticks:
    collisions = collide(pDict, vDict, aDict)
    if collisions > 0:
        # keep "safety" to ensure all collisions found
        ticks = currentTick + 10000
    updateValues(pDict, vDict, aDict)
    currentTick += 1

print("ran", ticks, "ticks, found", len(pDict), "particles remaining")
