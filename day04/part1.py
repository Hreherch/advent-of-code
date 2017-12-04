import sys

filename = sys.argv[1]
file = open(filename, 'r')

sum = 0

for line in file:
    passes = True
    passDict = {}
    for word in line.split():
        if word in passDict:
            passes = False
        else:
            passDict[word] = True

    if passes:
        sum += 1

print(sum)
