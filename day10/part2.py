import sys

filename = sys.argv[1]
file = open(filename, 'r')

string = []
inputs = []

for ch in file.read().strip():
    inputs.append(ord(ch))
inputs += [17, 31, 73, 47, 23]

for i in range(0, 256):
    string.append(i)

index = 0
skipSize = 0

for time in range(64):
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

denseHash = []
for startIndex in range(0, len(string), 16):
    denseHash.append(string[startIndex])
    for i in range(startIndex + 1, startIndex + 16):
        denseHash[-1] = denseHash[-1] ^ string[i]

for num in denseHash:
    print(format(num, "02X").lower(), end="")
print()
