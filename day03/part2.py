# Simulator to find your value.
# use w, a, s, d as the first input and the number of times you want to do it
# Probably would have been better to find the pattern :p

target = 347991

array = [[0] * 100 for _ in range(100)]
array[25][25] = 1
array[26][25] = 1

x = 26
y = 25
while True:
    mychoice = input("choice:")
    times = int(mychoice[1])
    mychoice = mychoice[0]

    for i in range(times):
        if mychoice == "d":
            x += 1
        elif mychoice == "w":
            y += 1
        elif mychoice == "a":
            x -= 1
        elif mychoice == "s":
            y -= 1

        print("adding:", x, y)

        array[x][y] = array[x-1][y-1] \
            + array[x][y-1] \
            + array[x+1][y-1] \
            + array[x-1][y] \
            + array[x][y] \
            + array[x+1][y] \
            + array[x-1][y+1] \
            + array[x][y+1] \
            + array[x+1][y+1]

    print()
    print(array[x-1][y+1], array[x][y+1], array[x+1][y+1])
    print(array[x-1][y], array[x][y], array[x+1][y])
    print(array[x-1][y-1], array[x][y-1], array[x+1][y-1])
