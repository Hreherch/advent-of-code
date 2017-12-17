# run like: python3 part1.py [your value]

import sys

n = int(sys.argv[1])
spinlock = [0]
index = 0

for i in range(1, 2018):
    index = ((index + n) % len(spinlock)) + 1
    firstHalf = spinlock[:index]
    secondHalf = spinlock[index:]
    spinlock = firstHalf + [i] + secondHalf

# print section of spinlock
print(spinlock[index-1:index+2])
