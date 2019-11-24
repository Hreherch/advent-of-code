import sys

def timeBetween(log1, log2):
    t = 0
    mins = []
    a = [log1[0], log1[1], log1[2], log1[3], log1[4]]
    while a[4] != log2[4]:
        mins.append(a[4])
        t += 1
        a[4] += 1
        if a[4] == 60:
            a[4] = 0
            a[3] += 1
            # we don't need to care about the other numbers
            # because of our problem input
    return t, mins

filename = sys.argv[1]
file = open(filename, 'r')
logs = []
for line in file:
    line = line.split()
    aSplit = line[0][1:].split("-")
    year, month, day = int(aSplit[0]), int(aSplit[1]), int(aSplit[2])
    aSplit = line[1][:-1].split(":")
    h, m = int(aSplit[0]), int(aSplit[1])
    a = line[3] if "#" not in line[3] else int(line[3][1:])
    logs.append((year, month, day, h, m, a))
file.close()

logs.sort()
i = 0
tracker = {} 
# have to go through all the logs before 
# determining the sleepiest
while i+1 < len(logs):
    guard = logs[i][5]
    while i+1 < len(logs):
        i += 1
        if logs[i][5] == "up":
            t, mins = timeBetween(logs[i-1], logs[i])
            for m in mins:
                if m not in tracker:
                    tracker[m] = {}
                tracker[m][guard] = tracker[m].get(guard, 0) + 1
        elif logs[i][5] != "asleep":
            break # new guard, break

timesSleptOn = -1
sleepyMinute = -1
sleepyGuard = -1
for minute in tracker:
    for guard in tracker[minute]:
        if tracker[minute][guard] > timesSleptOn:
            timesSleptOn = tracker[minute][guard]
            sleepyMinute = minute
            sleepyGuard = guard

print(sleepyGuard * sleepyMinute)
