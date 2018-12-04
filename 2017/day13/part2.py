# this is slow
import sys

filename = sys.argv[1]
file = open(filename, 'r')

scannerList = []

# (currentPosition, max index)
for line in file:
    line = line.strip().split(":")
    maxValue = int(line[1]) + int(line[1]) - 2
    scannerList.append([int(line[0]) % maxValue, maxValue])
delay = 0
while True:
    delay += 1
    hitScanner = False
    if delay % 100000 == 0:
        print(delay)
    for scanner in scannerList:
        scanner[0] += 1
        if scanner[0] == scanner[1]:
            scanner[0] = 0
            hitScanner = True

    if not hitScanner:
        print(delay)
        break
