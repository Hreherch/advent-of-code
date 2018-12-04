import sys

filename = sys.argv[1]
file = open(filename, 'r')
checksum = 0
for line in file:
    nums = line.split()
    for i in range(len(nums)):
        num1 = int(nums[i])
        for j in range(i+1, len(nums)):
            num2 = int(nums[j])
            n12 = num1 // num2
            n21 = num2 // num1
            if num1 % num2 == 0:
                checksum += n12
            elif num2 % num1 == 0:
                checksum += n21
                
print(checksum)
