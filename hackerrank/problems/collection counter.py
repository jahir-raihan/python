n = int(input())
sizes = list(map(int, input().split()))
res = 0
for i in range(int(input())):
    price = list(map(int, input().split()))
    if price[0] in sizes:
        res += price[1]
        sizes.remove(price[1])
print(res)