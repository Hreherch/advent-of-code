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

WORKERS = 5
available = []
delete = []
# get tasks with no requirements
for task in requires:
    if len(requires[task]) == 0:
        available.append(task)
        delete.append(task)

workers = [None, None, None, None, None]
workingOn = [None, None, None, None, None]
timeTaken = 0
while len(taskList) != len(tasks):
    # delete tasks (prevent RuntimeError)
    for task in delete:
        requires.pop(task)
    delete = []
    available.sort(reverse=True)
    # assign tasks if possible
    while None in workers and len(available) > 0:
        for i in range(WORKERS):
            if workers[i] == None:
                doNow = available.pop()
                workingOn[i] = doNow
                workers[i] = ord(doNow) - ord('A') + 61
                break # need to check while loop condition again
    # time marches forward
    while 0 not in workers:
        timeTaken += 1
        for i in range(WORKERS):
            if workers[i] != None:
                workers[i] -= 1
    # task was finished
    doneTaskIndex = workers.index(0)
    workers[doneTaskIndex] = None
    taskList.append(workingOn[doneTaskIndex])
    taskFinished = workingOn[doneTaskIndex]
    workingOn[doneTaskIndex] = None
    # find new tasks now that task is finished
    for task in requires:
        if taskFinished in requires[task]:
            requires[task].pop(requires[task].index(taskFinished))
            if len(requires[task]) == 0:
                available.append(task)
                delete.append(task)

print(timeTaken)