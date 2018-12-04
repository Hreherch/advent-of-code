import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

dancers = []
for ch in "abcdefghijklmnop":
    dancers.append(ch)

for move in file.read().split(","):
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

print("".join(dancers))
