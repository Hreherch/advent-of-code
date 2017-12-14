import sys

filename = sys.argv[1]
file = open(filename, 'r')

scanners = {}

for line in file:
    line = line.strip().split(":")
    scanners[int(line[0])] = int(line[1])

def scannerIsAtTop(position, length):
    index = 1 # starts at 1
    movingUp = True
    while position != 0:
        movement = 1 if movingUp else -1
        index += movement
        if index == 1 or index == length:
            movingUp = not movingUp
        position -= 1
    return index == 1
                

severity = 0
scannerList = list(scanners.keys())
scannerList.sort()
for scanner in scannerList:
    depth = scanner
    length = scanners[scanner]
    if scannerIsAtTop(depth, length):
        severity += depth * length

print(severity)
