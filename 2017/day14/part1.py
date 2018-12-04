def getKnotHash(stringIn):
    string = []
    inputs = []

    for ch in stringIn.strip():
        inputs.append(ord(ch))
    inputs += [17, 31, 73, 47, 23]

    for i in range(0, 256):
        string.append(i)

    index = 0
    skipSize = 0

    for time in range(64):
        for length in inputs:
            newList = []

            for i in range(index, index + length):
                i = i % 256
                newList.append(string[i])
            newList = newList[::-1] # reverse a list
                
            for i in range(index, index + length):
                string[i%256] = newList[i - index]

            index = index + length + skipSize
            skipSize += 1

    denseHash = []
    for startIndex in range(0, len(string), 16):
        denseHash.append(string[startIndex])
        for i in range(startIndex + 1, startIndex + 16):
            denseHash[-1] = denseHash[-1] ^ string[i]

    knotHash = ""
    for num in denseHash:
        knotHash += format(num, "02X").lower()
    return knotHash

valueDict = {
    "0": 0,
    "1": 1, # 1
    "2": 1, # 10
    "3": 2, # 11
    "4": 1, # 100
    "5": 2, # 101
    "6": 2, # 110
    "7": 3, # 111
    "8": 1, # 1000
    "9": 2, # 1001
    "a": 2, # 1010
    "b": 3, # 1011
    "c": 2, # 1100
    "d": 3, # 1101
    "e": 3, # 1110
    "f": 4
}

inUse = 0
for time in range(0, 128):
    hashInput = "ljoxqyyw-" + str(time)
    knotHash = getKnotHash(hashInput)
    for ch in knotHash:
        inUse += valueDict[ch]

print(inUse)
