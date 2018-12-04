# expected usage:
# python3 part1and2.py [input file] [# of iterations]
import sys

filename = sys.argv[1]
file = open(filename, 'r')

iterations = int(sys.argv[2])

def rotRight(arr):
    newImage = []
    for i in range(len(arr)):
        newImage.append([0] * len(arr))

    col = -1
    for itemRow in arr:
        row = 0
        for item in itemRow:
            newImage[row][col] = item
            row += 1
        col -= 1

    return newImage
            

def flipHorizontal(arr):
    newImg = []
    for oldRow in arr:
        newRow = []
        for elem in oldRow:
            newRow.append(elem)
        L = 0
        R = len(oldRow) - 1
        while L < R:
            newRow[L], newRow[R] = newRow[R], newRow[L]
            L += 1
            R -= 1
        newImg.append(newRow)
    return newImg

def stringToArray(string):
    arr = []
    for strRow in string.split("/"):
        row = []
        for ch in strRow:
            row.append(True if ch == "#" else False)
        arr.append(row)
    return arr

def arrayToString(arr):
    string = ""
    for row in arr:
        for elem in row:
            string += "#" if elem else "."
        string += "/"

    return string[:-1]

def generateImages(imageString):
    images = []
    arr = stringToArray(imageString)
    for i in range(2):
        for j in range(4):
            arr = rotRight(arr)
            images.append(arrayToString(arr))
        arr = flipHorizontal(arr)
    return images

superMap = {}
for line in file:
    line = line.split("=>")
    line[0] = line[0].strip()
    line[1] = line[1].strip()
    for image in generateImages(line[0]):
        if image in superMap:
            if superMap[image] != line[1]:
                print("error")
        else:
            superMap[image] = line[1]

# returns an 2D array of sub images based on imgStr
def splitter(imgStr):
    arr = stringToArray(imgStr)
    size = len(arr)
    # accidentally `cutSize = 3 if size % 3 == 0 else 2`, but order matters
    cutSize = 2 if size % 2 == 0 else 3
    imgArr = []
    for row in range(0, size, cutSize):
        imgArrRow = []
        for col in range(0, size, cutSize):
            img = []
            for rowOffset in range(cutSize):
                imgRow = []
                for colOffset in range(cutSize):
                    imgRow.append(arr[row + rowOffset][col + colOffset])
                img.append(imgRow)
            imgArrRow.append(img)
        imgArr.append(imgArrRow)

    return imgArr
            
# joins a 2D array of imgStrs into a single imgStr
def joiner(imgArr):
    imgStr = ""
    for row in imgArr:
        for rowInImg in range(len(row[0].split("/"))):
            for img in row:
                imgStr += img.split("/")[rowInImg]
            imgStr += "/"
    
    return imgStr[:-1]
        
img = ".#./..#/###"
for iteration in range(iterations):
    print("*")
    splitImg = splitter(img)

    for i in range(len(splitImg)):
        for j in range(len(splitImg[i])):
            splitImg[i][j] = superMap[arrayToString(splitImg[i][j])]

    img = joiner(splitImg)

print(img.count("#"))
