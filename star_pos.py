from dict_stars import hour, mins, angle

star_pos = []

for x in range(len(hour)):
    star_pos.append((int(angle[x]), float((hour[x]+"."+mins[x]))))
