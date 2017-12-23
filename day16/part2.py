import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

dancerStr = "abcdefghijklmnop"
dancers = []
for ch in "abcdefghijklmnop":
    dancers.append(ch)
moves = file.read().split(",")

# using n hard runs is a pretty rough solution, we could make the dancerMap incremental instead
n = 1000

for times in range(n):
    if times % 100 == 0:
        print(times)
    for move in moves:
        move = move.strip()
        if move[0] == "s":
            spin = int(move[1:])
            for i in range(spin):
                dancers = [dancers.pop()] + dancers
        elif move[0] == "x":
            match = re.match("x(\d+)\/(\d+)", move)
            index1 = int(match.group(1))
            index2 = int(match.group(2))

            dancers[index1], dancers[index2] = dancers[index2], dancers[index1]
        elif move[0] == "p":
            dancer1 = move[1]
            dancer2 = move[3]
            index1 = dancers.index(dancer1)
            index2 = dancers.index(dancer2)

            dancers[index1], dancers[index2] = dancers[index2], dancers[index1]

print("finished", n, "hard runs.. creating map.")

danceMap = []
for ch in dancerStr:
    danceMap.append(dancers.index(ch))

for time in range((1000000000-n)//n):
    print(time, "".join(dancers))
    newDancers = [0] * len(dancerStr)
    for i in range(len(danceMap)):
        newDancers[danceMap[i]] = dancers[i]
    dancers = newDancers

print("".join(dancers))
