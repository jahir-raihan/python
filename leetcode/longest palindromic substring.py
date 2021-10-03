s = "cbbd"
c = r = max_palindrome = index = 0

res = ''
for i in s:
    res += i
    res += '#'

res = '@#' + res + '&'
lps = [0]*len(res)
for i in range(1, len(res)-1):
    if i < r:
        lps[i] = min(lps[c - (i - c)], r-i)
    while res[i+lps[i]+1] == res[i-lps[i]-1]:
        lps[i] += 1

    if i + lps[i] > r:
        c = i
        r = i + lps[i]


for i in range(len(lps)):
    if lps[i] > max_palindrome:
        max_palindrome = lps[i]
        index = i

actual = ((index - max_palindrome + 1) - 2)//2
print(actual)
print(max_palindrome)
print(s[actual:actual + max_palindrome])
