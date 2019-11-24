import sys

filename = sys.argv[1]
file = open(filename, 'r')
fz = 0
for line in file:
    fz += int(line)
print(fz)
file.close()
