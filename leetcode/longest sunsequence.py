def longest_substring(s):
    dic = {}
    res = i = 0
    for j in range(len(s)):
        if s[j] in dic:
            i = max(i, (dic[s[j]]+1))
        res = max(res, (j-i+1))
        dic[s[j]] = j
    return res

longest_substring('abcabcbb')