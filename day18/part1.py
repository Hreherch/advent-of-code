import sys

filename = sys.argv[1]
file = open(filename, 'r')

instructions = []
registers = {}
for command in file:
    instructions.append(command.split())

def isDigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
        

def getRegisterValue(registers, key):
    if key in registers:
        return registers[key]
    else:
        registers[key] = 0
        return 0

def getValue(registers, commandValue):
    if isDigit(commandValue):
            return int(commandValue)
    return getRegisterValue(registers, commandValue)

index = 0 # current instruction
recentSound = None
while index >= 0 and index < len(instructions):
    command = instructions[index]
    cType = command[0]
    print(index, command, registers)
    if cType == "snd":
        recentSound = getRegisterValue(registers, command[1])
    elif cType == "set":
        registers[command[1]] = getValue(registers, command[2])
    elif cType == "add":
        getRegisterValue(registers, command[1]) # force init
        registers[command[1]] += getValue(registers, command[2])
    elif cType == "mul":
        getRegisterValue(registers, command[1])
        registers[command[1]] *= getValue(registers, command[2])
    elif cType == "mod":
        getRegisterValue(registers, command[1])
        registers[command[1]] = registers[command[1]] % getValue(registers, command[2])
    elif cType == "rcv":
        if getValue(registers, command[1]) != 0:
            print("recovered value:", recentSound)
            break # end program since we've found the value
    elif cType == "jgz":
        if getValue(registers, command[1]) > 0:
            index += getValue(registers, command[2])
            continue
    index += 1
