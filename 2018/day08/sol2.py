import sys

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read()
data = data.split()

# wrapper to not write int(...) 100 times
def getData(p):
    #print("reading data at p={}:".format(p), data[p])
    return int(data[p])

# pointer should be at the children definition on a node 
# returns (nodeValue, shift (amount that the pointer moved))
def sumMetadata(pointer):
    value = 0
    shift = 2
    children = getData(pointer)
    mdEntries = getData(pointer+1)
    pointer += shift
    # no children: simply the value of the metadata entries
    if children == 0:
        for i in range(mdEntries):
            shift += 1
            value += getData(pointer)
            pointer += 1
    # children: get children values, then sum the indexed values
    else:
        childValues = []
        for i in range(children):
            childValue, gainedShift = sumMetadata(pointer)
            childValues.append(childValue)
            shift += gainedShift
            pointer += gainedShift
        for i in range(mdEntries):
            shift += 1
            index = getData(pointer) - 1
            pointer += 1
            if index < len(childValues):
                value += childValues[index]
    return value, shift

print(sumMetadata(0)[0])