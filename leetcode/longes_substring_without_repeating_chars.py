string = "abcabcbb"
i = j = 0
max_s = 0
dic = {}
while True:
    try:
        if string[j] in dic:
            dic = {}
            i += 1
            max_s = max(max_s, j-i)
            j = j - 1
        else:
            dic[string[j]] = True
            j += 1
            max_s = max(max_s, j - i)
    except:
        break

print(max_s)