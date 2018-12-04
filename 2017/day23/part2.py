# Watch as I slowly but surely translate assembly (.-.)

''' Program 0 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
set b 93
set c b

jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000

set f 1
set d 2
set e 2

set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8 [set g d]

sub d -1
set g d
sub g b
jnz g -13 [set e 2]

jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
'''

''' Program 1 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# default a = 1
a = 1
b = c = d = e = f = g = h = 0

# program start
b = 109300
c = b + 17000

g = 1 # to start loop in python without skipping it
while g != 0:
    f = 1
    d = 2
    e = 2
    g = d
    while g != 0:
        # copy of the above two instructions to maintain loop integrity
        e = 2
        g = d
        while g != 0:
            g = d
            g *= e
            g -= b
            if g == 0:
                f = 0
            e += 1
            g = e
            g -= b
        d += 1
        g = d
        g -= b
    if f == 0:
        h += 1
    g = b
    g -= c
    if g == 0:
        print("h is finally:", h)
        exit()
    b += 17
'''

''' Program 2 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# default a = 1
a = 1
b = c = d = e = f = g = h = 0

# program start
b = 109300
c = b + 17000

g = 1 # to start loop in python without skipping it
while g != 0:
    f = 1
    d = 2
    e = 2
    g = d
    while d != b:
        # copy of the above two instructions to maintain loop integrity
        e = 2
        g = d
        while e != b:
            g = (d * e) - b
            if g == 0:
                f = 0
            e += 1
        d += 1
    if f == 0:
        h += 1
    g = b - c
    if g == 0:
        print("h is finally:", h)
        exit()
    b += 17
'''


''' final program  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * '''
# h is only increased when we increase b by 17 (outermost loop)
# h is only increased if (c*d) == b (inner loop, when set f 0)
# => count the number of composite numbers in range(109300, 126301, 17)
composites = 0
for i in range(109300, 126301, 17):
    for x in range(2, i):
        if i % x == 0:
            composites += 1
            break;

print(composites)
