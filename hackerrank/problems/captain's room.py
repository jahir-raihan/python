_ = input()
di = {}
lis = [int(i) for i in input().split()]
for i in lis:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

print(min(di, key=di.get))