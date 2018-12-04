import sys

filename = sys.argv[1]
file = open(filename, 'r')

stepsTaken = 0
instructions = []

for line in file:
    instructions.append(int(line))

index = 0
while index >= 0 and index < len(instructions):
    instruction = instructions[index]
    instructions[index] += 1
    index += instruction

    stepsTaken += 1

print(stepsTaken)
