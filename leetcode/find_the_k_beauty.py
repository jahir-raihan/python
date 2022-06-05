num = 30003
s_num = '30003'
k = 3
res = 0
j = k
for i in range(len(str(num))):

    tmp = s_num[i:j]
    try:
        var = num % int(tmp)
        if num % int(tmp) == 0:
            res += 1
        if j == len(s_num):
            break
        j += 1

    except:
        if j == len(s_num):
            break
        j += 1
        pass
print(res)