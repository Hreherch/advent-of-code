import sys

# no duplicates in file
filename = sys.argv[1]
file = open(filename, 'r')

bridges = {}
for line in file:
    component = line.strip()
    ports = component.split("/")
    ports[0], ports[1] = int(ports[0]), int(ports[1])
    if ports[0] in bridges:
        bridges[ports[0]].append(component)
    else:
        bridges[ports[0]] = [component]
    if ports[1] in bridges:
        bridges[ports[1]].append(component)
    else:
        bridges[ports[1]] = [component]

# goes over (strength, depth) pairs and returns by largest depth, then largest strength
def betterMax(values):
    if len(values) == 0:
        return (0, 0)
    if len(values) == 1:
        return values[0]

    bestDepth = 0
    for value in values:
        if value[1] > bestDepth:
            bestDepth = value[1]

    deepValues = []
    for value in values:
        if bestDepth == value[1]:
            deepValues.append(value)

    bestStr = 0
    for value in deepValues:
        if value[0] > bestStr:
            bestStr = value[0]

    for value in values:
        if value[0] == bestStr:
            return value

# This is ugly, but I love all children equally...
def findMax(start, end, bridges, visited):
    value = (start + end, 1)
    
    print("looking at", start, ":", end)
    optionValues = []
    for option in bridges[end]:
        if option not in visited:
            optionValues.append(option)

    if len(optionValues) == 0:
        return value

    # APPARENTLY, if you write [value] here, everything breaks :)
    values = [(0, 0)]
    for option in optionValues:
        ports = option.split("/")
        ports[0], ports[1] = int(ports[0]), int(ports[1])
        if ports[0] == end:
            newVisited = dict(visited)
            newVisited[option] = True
            values.append(findMax(ports[0], ports[1], bridges, newVisited))
        else:
            newVisited = dict(visited)
            newVisited[option] = True
            values.append(findMax(ports[1], ports[0], bridges, newVisited))

    bestValue = betterMax(values)
    return (start + end + bestValue[0], 1 + bestValue[1])

result = []
for option in bridges[0]:
    port = 0
    for portCheck in option.split("/"):
        portCheck = int(portCheck)
        if portCheck != 0:
            visited = {}
            visited[option] = True
            result.append(findMax(0, portCheck, bridges, visited))

result = betterMax(result)

print(result)
