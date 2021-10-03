t = 9
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
j = 1
res = []

for k in range(len(arr)):
    if sum(arr[i:j]) == t:
        res.append((arr[i:j]))
        i += 1
        j = i + 1
    j += 1