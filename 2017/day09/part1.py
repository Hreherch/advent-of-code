import sys

filename = sys.argv[1]
file = open(filename, 'r')

def readGarbage(stream):
    score = 0
    depth = 0
    inGarbage = False
    ignoreNext = False

    for ch in stream:
        if ignoreNext:
            ignoreNext = False
            continue

        if ch == "!":
            ignoreNext = True
            continue

        if inGarbage:
            if ch == ">":
                inGarbage = False
            continue

        if ch == "<":
            inGarbage = True
            continue

        if ch == "{":
            depth += 1
            continue

        if ch == "}":
            score += depth
            depth -= 1
            continue
    
    return score

print(readGarbage(file.read()))
