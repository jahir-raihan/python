import re
a = 'aaadaa'
b = 'aa'
m = re.search(b, a)
print(m.start(), m.end())
print(m.start())