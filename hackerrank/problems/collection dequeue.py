from collections import deque
d = deque()
dic = {
    'append': lambda x: d.append(x), 'appendleft': lambda x: d.appendleft(x), 'pop': lambda : d.pop(),'popleft': lambda: d.popleft()
}
for _ in range(int(input())):
    n = input().split()
    try:
        dic[n[0]](n[1])
    except:
        dic[n[0]]()
print(*d)
