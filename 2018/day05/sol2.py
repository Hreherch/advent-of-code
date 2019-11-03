import sys
import re

reactions = {}
for i in range(ord('a'), ord('z')+1):
    ch = chr(i)
    reactions[ch + ch.upper()] = True
    reactions[ch.upper() + ch] = True

regexReactions = ""
for i in range(ord('a'), ord('z')+1):
    ch = chr(i)
    chU = ch.upper()
    regexReactions += ch + chU + "|" + chU + ch + "|"
regexReactions = regexReactions[0:-1] # remove last "|"
regexReactions = re.compile(regexReactions)

# v. slow...
def react(polymer, ch):
    polymer = re.sub("{}|{}".format(ch, ch.upper()), "", polymer)
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
    return len(polymer)

# equivalently slow... lol
def reactv2(polymer, ch):
    polymer = re.sub("{}|{}".format(ch, ch.upper()), "", polymer)
    l = 0
    while l != len(polymer):
        l = len(polymer)
        polymer = re.sub(regexReactions, "", polymer)
    return len(polymer)

filename = sys.argv[1]
file = open(filename, 'r')
polymer = file.read().strip()
file.close()

l = 10e9
for i in range(ord('a'), ord('z')+1):
    print("reacting", chr(i), l)
    t = reactv3(polymer, chr(i)) 
    if t < l:
        l = t

print(l)
