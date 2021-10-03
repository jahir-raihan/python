M, m = int(input()), set(int(i) for i in input().split())
N, n = int(input()), set(int(i) for i in input().split())
print(*sorted(list(m.difference(n)) + list(n.difference(m))), sep='\n')

# regex is valid or not

import re

for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print(False)





