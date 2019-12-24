stars = []
stars2 = []
with open('coords.txt', 'r') as s:
    for x in s:
        stars.append(x.split(' '))

hour = []
mins = []
#sec = []
angle = []

for d in stars:
    hour.append(d[0])
    mins.append(d[1])
    #sec.append(d[2])
    angle.append(d[3])
