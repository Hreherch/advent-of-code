import sys

filename = sys.argv[1]
file = open(filename, 'r')

hasChildren = {}
isChild = {}

for line in file:
    childParentArray = line.split("->")

    if len(childParentArray) <= 1:
        continue

    parent = childParentArray[0].split()[0].strip()
    children = childParentArray[1].split(", ")

    if parent not in hasChildren:
        hasChildren[parent] = True

    for child in children:
        child = child.strip()
        if child not in isChild:
            isChild[child] = True

for parent in hasChildren:
    if parent not in isChild:
        print(parent)
