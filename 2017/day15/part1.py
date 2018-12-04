import sys

filename = sys.argv[1]
file = open(filename, 'r')

valueA = int(file.readline().strip().split()[-1])
valueB = int(file.readline().strip().split()[-1])
bitmask = 0b1111111111111111

class generator:
    def __init__(self, value, factor):
        self.previousValue = value
        self.factor = factor

    def getNext(self):
        newValue = (self.previousValue * self.factor) % 2147483647
        self.previousValue = newValue
        return newValue

a = generator(valueA, 16807)
b = generator(valueB, 48271)

count = 0
for times in range(40000000):
    if times % 100000 == 0:
        print(times)
    if (a.getNext() & bitmask) == (b.getNext() & bitmask):
        count += 1
print(count)
