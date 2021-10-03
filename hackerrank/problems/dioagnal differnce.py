def dioagnal_differnce(array, n):
    d1 = d2 = 0
    for i in range(n):
        d1 += array[i][i]
        d2 += array[i][n-1-i]
    return abs(d1-d2)


n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
dioagnal_differnce(array, n)
