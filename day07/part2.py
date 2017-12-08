import sys
import re

filename = sys.argv[1]
file = open(filename, 'r')

weights = {}
parents = {}
isChild = {}

for line in file:
    match = re.match("([a-z]+) \((\d+)\)", line)
    parent = match.group(1)
    weights[parent] = int(match.group(2))
    
    match = re.search("-> ([a-z, ]+)", line)
    if match:
        children = match.group(1).split(", ")
        parents[parent] = children
        for child in children:
            if child not in isChild:
                isChild[child] = True

root = ""
for parent in parents:
    if parent not in isChild:
        root = parent

def findProblem(node):
    childWeights = []
    if node in parents:
        children = parents[node]
        for child in children:
            childWeights.append(findProblem(child))
            
    different = -1
    weightNeeded = 0
    for i in range(len(childWeights)):
        numDiffer = 0
        for j in range(len(childWeights)):
            if i == j:
                continue
            if childWeights[i] != childWeights[j]:
                numDiffer += 1
                weightNeeded = abs(childWeights[i] - childWeights[j])

        if numDiffer > 1:
            different = i
        if different != i:
            break

    if different != -1:
        problem = parents[node][different]
        print(problem, "should be", weightNeeded, "units lighter, currently:", weights[problem])

    
    return weights[node] + sum(childWeights)

findProblem(root)
