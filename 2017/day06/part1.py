import sys

filename = sys.argv[1]
file = open(filename, 'r')

memoryDict = {}
banks = []

for line in file:
    for blocks in line.split():
        banks.append(int(blocks))

memoryDict[tuple(banks)] = True

cycles = 0
while True:
    maxValue = max(banks)
    index = banks.index(maxValue)

    banks[index] = 0

    for count in range(maxValue):
        index = (index+1)%len(banks)
        banks[index] += 1

    cycles += 1

    bank_t = tuple(banks)
    if bank_t in memoryDict:
        print(cycles)
        break;
    else:
        memoryDict[bank_t] = True
