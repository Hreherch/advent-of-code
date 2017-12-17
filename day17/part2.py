# run like: python3 part2.py [your step value]

import sys

n = int(sys.argv[1])
spinlockLen = 1
check = 1
index = 0
value = None

for i in range(1, 50000001):
    index = ((index + n) % spinlockLen) + 1
    if index == check:
        value = i
        print("new value:", value)
    elif index == check - 1:
        check += 1
    spinlockLen += 1

print("Final answer:", value)
