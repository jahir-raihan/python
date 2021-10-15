ran = list(map(int, input().split()))

for i in range(ran[0], ran[1]+1):
    if i % 2 != 0:
        print(i, end=' ')
