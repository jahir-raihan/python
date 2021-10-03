di = {}
for _ in range(int(input())):
    string = input()
    if string in di:
        di[string] += 1
    else:
        di[string] = 1
print(len(di))

print(*di.values())
