import sys

filename = sys.argv[1]
file = open(filename, 'r')

tasks = {}
taskList = []
requires = {}
requiredFor = {}
for line in file:
    line = line.split()
    before = line[1] 
    then = line[7]

    # register tasks
    tasks[before] = False
    tasks[then] = False

    # fill the requirement graph
    if then not in requires:
        requires[then] = []
    requires[then].append(before)
    if before not in requires:
        requires[before] = []

file.close()

available = []
delete = []
# get tasks with no requirements
for task in requires:
    if len(requires[task]) == 0:
        available.append(task)
        delete.append(task)

while len(taskList) != len(tasks):
    # delete tasks (prevent RuntimeError)
    for task in delete:
        requires.pop(task)
    delete = []
    available.sort(reverse=True)
    doNow = available.pop()
    taskList.append(doNow)
    for task in requires:
        if doNow in requires[task]:
            requires[task].pop(requires[task].index(doNow))
            if len(requires[task]) == 0:
                available.append(task)
                delete.append(task)

print("".join(taskList))