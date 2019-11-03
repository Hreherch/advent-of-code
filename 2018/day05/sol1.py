import sys

filename = sys.argv[1]
file = open(filename, 'r')
polymer = file.read().strip()
file.close()

reactions = {}
for i in range(ord('a'), ord('z')+1):
    ch = chr(i)
    reactions[ch + ch.upper()] = True
    reactions[ch.upper() + ch] = True

rx = True
while rx:
    rx = False
    pos = 0
    while pos+1 < len(polymer):
        if polymer[pos:pos+2] in reactions:
            polymer = polymer[0:pos] + polymer[pos+2:]
            rx = True
        else:
            pos += 1

print(len(polymer))