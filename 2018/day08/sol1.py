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
# returns (sumMetadata, shift (amount that the pointer moved))
def sumMetadata(pointer):
    metadataSum = 0
    shift = 2
    children = getData(pointer)
    mdEntries = getData(pointer+1)
    pointer += shift
    for i in range(children):
        gainedSum, gainedShift = sumMetadata(pointer)
        metadataSum += gainedSum
        shift += gainedShift
        pointer += gainedShift
    for i in range(mdEntries):
        shift += 1
        metadataSum += getData(pointer)
        pointer += 1
    return metadataSum, shift

print(sumMetadata(0)[0])