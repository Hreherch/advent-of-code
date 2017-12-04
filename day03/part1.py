target = 347991

x = 1
while x * x < target:
    print(x, x*x, target)
    x += 1

sumSubbed = 0
current = x * x

while current != target:
    current -= 1
    sumSubbed += 1

print(sumSubbed, "side length:", x)

# x is the number of steps to get to bottom-right
# sumSubbed is the number of steps to get from bottom-right to target
# x - sumSubbed should be the manhattan distance (but it's off by one *shrug*)
