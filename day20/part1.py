import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

aDict = {}
vDict = {}
pDict = {}
winners = {}

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

# returns dictionary: {distance: particleId} and {particleId: distance}
def calculateDistances(pDict):
    p_dDict = {}
    d_pDict = {}

    for key in pDict:
        d = pDict[key]
        d = abs(d[0]) + abs(d[1]) + abs(d[2])
        if d not in d_pDict:
            d_pDict[d] = [key]
        else:
            d_pDict[d] += [key]
        p_dDict[key] = d

    return d_pDict, p_dDict

def updateValues(pDict, vDict, aDict):
    for key in range(len(aDict)):
        for i in range(3):
            vDict[key][i] += aDict[key][i]
        for i in range(3):
            pDict[key][i] += vDict[key][i]

print("Running test with 10000 ticks")

for times in range(10000):
    d_pDict, p_dDict = calculateDistances(pDict)
    minKey = min(list(d_pDict.keys()))
    minParticles = d_pDict[minKey]
    for particle in minParticles:
        if particle not in winners:
            winners[particle] = 1
        else:
            winners[particle] += 1
    updateValues(pDict, vDict, aDict)

print("in 10000 ticks, it seems like...")

maxValue = max(list(winners.values()))
for key in winners:
    if winners[key] == maxValue:
        print(key, "is the closest particle")
        break
