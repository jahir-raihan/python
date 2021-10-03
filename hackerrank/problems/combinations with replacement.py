from itertools import combinations_with_replacement
s, n = input().split()
[print(''.join(c)) for c in combinations_with_replacement(sorted(s), int(n))]
