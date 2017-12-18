import sys

filename = sys.argv[1]
file = open(filename, 'r')

instructions = []
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

# returns index, and a sndQueue
def runProgram(instructions, index, registers, rcvQueue):
    sndQueue = []
    while len(rcvQueue) > 0 or instructions[index][0] != "rcv":
        command = instructions[index]
        cType = command[0]
        if cType == "snd":
            sndQueue.append(getValue(registers, command[1]))
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
            getRegisterValue(registers, command[1])
            registers[command[1]] = rcvQueue.pop(0)
        elif cType == "jgz":
            if getValue(registers, command[1]) > 0:
                index += getValue(registers, command[2])
                continue
        index += 1

    return index, sndQueue 

p0 = [0, {"p": 0}]
p1 = [0, {"p": 1}]
p1Sent = 0
p0Queue = []
p1Queue = []

while True:
    p0[0], p1Queue = runProgram(instructions, p0[0], p0[1], p0Queue)
    p1[0], p0Queue = runProgram(instructions, p1[0], p1[1], p1Queue)
    sent = len(p0Queue)
    if sent == 0:
        print("p1 sent", p1Sent, "values")
        break
    p1Sent += sent
