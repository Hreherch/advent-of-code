# Borrows mathematical concept from:
# https://stackoverflow.com/questions/1838656/how-do-i-represent-a-hextile-hex-grid-in-memory

import sys
filename = sys.argv[1]
file = open(filename, 'r')

steps = file.read().split(",")

commands = []

for step in steps:
    step = step.strip()
    commands.append(step)

# Let N be (0, +y, -z), counter: S
# Let NW (-x, +y, 0) counter: SE
# Let NE (+x, 0, -z)
currentMax = 0
x = y = z = 0
for step in commands:
    if step == "n":
        y += 1
        z -= 1
    elif step == "s":
        y -= 1
        z += 1
    elif step == "nw":
        x -= 1
        y += 1
    elif step == "se":
        x += 1
        y -= 1
    elif step == "ne":
        z -= 1
        x += 1
    elif step == "sw":
        z += 1
        x -= 1
    
    thisMax = max(abs(x), abs(y), abs(z))
    if thisMax > currentMax:
        currentMax = thisMax

print(currentMax)
