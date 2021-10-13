res = 0
res_lis = []
num = int(input())

for i in range(1, num+1):
    if num % i == 0 :
        res += 1
        res_lis.append(i)

print(res)
print(*res_lis)