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

# This is ugly, but I love all children equally...
def findMax(start, end, bridges, visited):
    value = start + end
    
    print("looking at", start, ":", end)
    optionValues = []
    for option in bridges[end]:
        if option not in visited:
            optionValues.append(option)
    print("options", optionValues)

    if len(optionValues) == 0:
        print("returning value:", value)
        return value

    values = [0]
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
                

    print(values)
    print("returning value:", max(values) + value)
    return max(values) + value

    

result = []
for option in bridges[0]:
    port = 0
    for portCheck in option.split("/"):
        portCheck = int(portCheck)
        if portCheck != 0:
            visited = {}
            visited[option] = True
            result.append(findMax(0, portCheck, bridges, visited))

print(max(result))
    
