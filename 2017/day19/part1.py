import sys

filename = sys.argv[1]
file = open(filename, 'r')

pipes = []

for line in file:
    row = []
    for ch in line:
        if ch != "\n":
            row.append(ch)
    pipes.append(row)

startIndex = None
for i in range(len(pipes[0])):
    ch = pipes[0][i]
    if ch == "|":
        startIndex = i
        break

# returns: vY, vX
def changeVelocity(pipes, y, x, vY, vX):
    up = down = left = right = None
    if y-1 > 0: 
        up = pipes[y-1][x]
    if y+1 < len(pipes):
        down = pipes[y+1][x]
    if x+1 < len(pipes[y]):
        right = pipes[y][x+1]
    if x-1 > 0:
        left = pipes[y][x-1]

    up = up == '|'
    down = down == '|'
    right = right == '-'
    left = left == '-'

    # if valid movement AND not already moving that way
    if up and vY != 1:
        return -1, 0
    if down and vY != -1:
        return 1, 0
    if left and vX != -1:
        return 0, -1
    if right and vX != 1:
        return 0, 1
    return 0, 0


location = [0, startIndex]
vY = 1
vX = 0
sentence = ""
while True:
    y = location[0]
    x = location[1]
    ch = pipes[y][x]

    if ch == ' ':
        print(sentence)
        break

    if ch == "+":
        vY, vX = changeVelocity(pipes, y, x, vY, vX)
    elif ch.isalnum():
        sentence += ch

    location[0], location[1] = y + vY, x + vX
