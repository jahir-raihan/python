n, Query = map(int, input().split())
last_number = 0
arr = [[]]*n

for _ in range(Query):
    query, x, y = list(map(int, input().split()))
    if query == 1:
        arr[(x ^ last_number) % n].append(y)
    if query == 2:
        j = (x ^ last_number) % n
        idx = arr[j]
        length = len(idx)
        last_number = arr[j][y % length]
        print(last_number)
