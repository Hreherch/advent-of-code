import sys

filename = sys.argv[1]
file = open(filename, 'r')
fzList = []
for line in file:
    fzList.append(int(line))
file.close()

fz = 0
i = 0
seen = {}
while True:
    if fz not in seen:
        seen[fz] = True
    else:
        print(fz)
        break
    fz += fzList[i]
    i = (i + 1) % len(fzList)
