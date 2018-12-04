tape = {}
state = "A"
position = 0

# returns newPosition, state
def doATuring(tape, state, position, curVal):
    if state == "A":
        if curVal == 0:
            tape[position] = 1
            position += 1
            state = "B"
        else:
            tape[position] = 0
            position += 1
            state = "F"

    elif state == "B":
        if curVal == 0:
            tape[position] = 0
            position -= 1
            state = "B"
        else:
            tape[position] = 1
            position -= 1
            state = "C"

    elif state == "C":
        if curVal == 0:
            tape[position] = 1
            position -= 1
            state = "D"
        else:
            tape[position] = 0
            position += 1
            state = "C"
            
    elif state == "D":
        if curVal == 0:
            tape[position] = 1
            position -= 1
            state = "E"
        else:
            tape[position] = 1
            position += 1
            state = "A"

    elif state == "E":
        if curVal == 0:
            tape[position] = 1
            position -= 1
            state = "F"
        else:
            tape[position] = 0
            position -= 1
            state = "D"

    elif state == "F":
        if curVal == 0:
            tape[position] = 1
            position += 1
            state = "A"
        else:
            tape[position] = 0
            position -= 1
            state = "E"

    return position, state

for steps in range(12964419):
    if steps % 100000 == 0:
        print(steps) 
    curVal = 0 if position not in tape else tape[position]
    position, state = doATuring(tape, state, position, curVal)

print(sum(list(tape.values())))
