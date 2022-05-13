import re

s = 'ab'
pattern = '.*c'
x = re.match(pattern, s)
try:
    if s == x.group():
        print(True)
    else:
        print(False)
except:
    print(False)