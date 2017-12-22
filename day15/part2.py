import sys
import math

filename = sys.argv[1]
file = open(filename, 'r')

valueA = int(file.readline().strip().split()[-1])
valueB = int(file.readline().strip().split()[-1])
bitmask = 0b1111111111111111

class generator:
    def __init__(self, value, factor, multiple):
        self.previousValue = value
        self.factor = factor
        self.multiple = multiple

    def getNext(self):
        newValue = (self.previousValue * self.factor) % 2147483647
        while newValue % self.multiple:
            # I spent an hour debugging my program because I used self.previousValue again :(
            newValue = (newValue * self.factor) % 2147483647
        self.previousValue = newValue
        return newValue

a = generator(valueA, 16807, 4)
b = generator(valueB, 48271, 8)

count = 0
for times in range(5000000):
    if times % 100000 == 0:
        print(times)
    if (a.getNext() & bitmask) == (b.getNext() & bitmask):
        count += 1
print(count)
