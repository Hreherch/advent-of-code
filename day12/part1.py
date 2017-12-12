import sys

filename = sys.argv[1]
file = open(filename, 'r')

nodeMap = {}

for line in file:
    split = line.split("<->")
    host = int(split[0])
    targets = split[1]
    nodeMap[host] = []
    for target in targets.split(","):
        target = int(target.strip())
        nodeMap[host].append(target)

def bfs(node, nodeMap):
    visited = {}
    queue = [node]
    while len(queue) > 0:
        node = queue.pop()

        if node in visited:
            continue

        visited[node] = True

        for child in nodeMap[node]:
            if child not in visited:
                queue.append(child)

    return len(visited)

print(bfs(0, nodeMap))
