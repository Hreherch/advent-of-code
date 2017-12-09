import sys

filename = sys.argv[1]
file = open(filename, 'r')

def readGarbage(stream):
    stream = stream.strip()
    garbageCount = 0
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
            else:
                garbageCount += 1
            continue

        if ch == "<":
            inGarbage = True
            continue
    
    return garbageCount

print(readGarbage(file.read()))
