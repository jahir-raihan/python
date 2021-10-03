from itertools import groupby
groups = []
keys = []
tup = []
for k, g in groupby(input(), lambda x: x[0]):
    groups.append(list(g))    # Store group iterator as a list
    keys.append(k)

for i in range(len(groups)):
    count = groups[i].count(keys[i])
    tup.append((count, int(keys[i]))) # if you want to add it as a string just remove the int func at this line .

print(*tup)