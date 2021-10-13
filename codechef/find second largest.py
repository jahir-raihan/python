res = []
for _ in range(3):
    res.append(int(input()))
res.remove(max(res))
print(max(res))
