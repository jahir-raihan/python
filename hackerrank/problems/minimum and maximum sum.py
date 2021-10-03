l = list(map(int, input().split()))
mini = l[:]
minimum = maximum = 0
for i in range(len(l)-1):
    minimum += min(mini)
    maximum += max(l)
    mini.remove(min(mini))
    l.remove(max(l))
print(minimum,maximum)
