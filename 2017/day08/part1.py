import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

registers = {}
types = {}

for line in file:
    commands = line.split()

    target = commands[0]
    action = commands[1]
    value = int(commands[2])

    check = commands[4]
    checkType = commands[5]
    checkValue = int(commands[6])

    if target not in registers:
        registers[target] = 0

    if check not in registers:
        registers[check] = 0

    shouldPerformAction = False
    if checkType == "<=":
        shouldPerformAction = registers[check] <= checkValue
    elif checkType == "!=":
        shouldPerformAction = registers[check] != checkValue
    elif checkType == ">=":
        shouldPerformAction = registers[check] >= checkValue
    elif checkType == "<":
        shouldPerformAction = registers[check] < checkValue
    elif checkType == ">":
        shouldPerformAction = registers[check] > checkValue
    elif checkType == "==":
        shouldPerformAction = registers[check] == checkValue

    if shouldPerformAction:
        if action == "inc":
            registers[target] += value
        elif action == "dec":
            registers[target] -= value

print(max(list(registers.values())))
