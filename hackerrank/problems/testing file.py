t = 7
arr = [1, 7, 4, 3, 1, 2, 1, 5, 1]
i = 0
j = 1
res = []

for k in range(len(arr)):
    n = sum(arr[i:j])
    if n == t:
        res.append((arr[i:j]))
        j += 1
        i += 1
    elif n > t:
        i += 1
    else:
        j += 1