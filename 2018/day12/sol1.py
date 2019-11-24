import sys
from collections import deque

filename = sys.argv[1]
file = open(filename, 'r')

initialState = ""
patterns = {}
for line in file:
    if "=>" in line:
        line = line.split()
        patterns[line[0]] = True if line[2] == "#" else False
    elif "initial" in line:
        line = line.split()
        initialState = line[2]

class Garden:
    def __init__(self, initState):
        self.garden = deque()
        # add 5 pots of padding
        for i in range(5):
            self.garden.append(False)
        self.zeroIndex = 5
        for ch in initState:
            self.garden.append(True if ch == "#" else False)
        # add 5 pots of padding
        for i in range(5):
            self.garden.append(False)

    def checkPads(self):
        # count number of spaces until we hit a plant
        firstPlantIndex = 0
        while not self.garden[firstPlantIndex]:
            firstPlantIndex += 1
        # Ensure left side is padded with 5 pots
        if firstPlantIndex < 5:
            while firstPlantIndex != 5:
                self.zeroIndex += 1
                firstPlantIndex += 1
                self.garden.appendleft(False)
        if firstPlantIndex > 5:
            while firstPlantIndex != 5:
                self.zeroIndex -= 1
                firstPlantIndex -= 1
                self.garden.popleft()

        # ensure right side is padded with pots
        # (doesn't affect zero-index)
        firstPlantIndex = -1
        while not self.garden[firstPlantIndex]:
            firstPlantIndex -= 1
        if firstPlantIndex > -6:
            while firstPlantIndex != -6:
                firstPlantIndex -= 1
                self.garden.append(False)
        if firstPlantIndex < -6:
            while firstPlantIndex != -6:
                firstPlantIndex += 1
                self.garden.pop()

    def live(self):
        s = "....." # we pad by 5
        for i in range(5, len(self.garden)):
            pot = "#" if self.garden[i] else "."
            s = s[1:] + pot
            self.garden[i-2] = patterns.get(s, False)
        self.checkPads()

    def score(self):
        print("zero is", self.zeroIndex, len(self.garden))
        total = 0
        v = -1
        for i in range(self.zeroIndex-1, -1, -1):
            if self.garden[i]:
                total += v
            v -= 1
        v = 1
        for i in range(self.zeroIndex+1, len(self.garden)):
            if self.garden[i]:
                total += v
            v += 1
        return total

    def __str__(self):
        s = ""
        for pot in self.garden:
            s += "#" if pot else "."
        return s

g = Garden(initialState)
for i in range(10000):
    print(i, len(g.garden), g.zeroIndex)
    g.live()
    #print(g)
print(g.score())