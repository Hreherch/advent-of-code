import sys

filename = sys.argv[1]
file = open(filename, 'r')

string = []
inputs = file.read().split(",")

for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

for i in range(0, 256):
    string.append(i)

index = 0
skipSize = 0

for length in inputs:
    newList = []

    for i in range(index, index + length):
        i = i % 256
        newList.append(string[i])
    newList = newList[::-1] # reverse a list
        
    for i in range(index, index + length):
        string[i%256] = newList[i - index]

    index = index + length + skipSize
    skipSize += 1

print(string)
