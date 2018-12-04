import sys

filename = sys.argv[1]
file = open(filename, 'r')
checksum = 0
for line in file:
    nums = line.split()
    maxNum = minNum = int(nums[0])
    for num in nums:
        num = int(num)
        if maxNum < num:
            maxNum = num
        elif minNum > num:
            minNum = num
    checksum += maxNum - minNum

print(checksum)
