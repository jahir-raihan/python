from collections import defaultdict
n, m = map(int, input().split())
dic = defaultdict(list)
for i in range(1, n+1):
    dic[input()].append(i)

for i in range(m):
    m = input()
    print(dic[m] if m in dic else -1)

