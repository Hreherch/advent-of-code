import sys

filename = sys.argv[1]
file = open(filename, 'r')

ids = []
for line in file:
    ids.append(line.strip())
file.close()

for i in range(0, len(ids)):
    for j in range(i+1, len(ids)):
        dist = 0
        for x in range(0, len(ids[i])):
            if ids[i][x] != ids[j][x]:
                dist += 1
                if dist > 1: break
        if dist == 1:
            for x in range(0, len(ids[i])):
                if ids[i][x] != ids[j][x]:
                    print(ids[i][0:x] + ids[i][x+1:])
                    

            


        


