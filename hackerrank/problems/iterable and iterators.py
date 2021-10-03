from itertools import combinations

_, s, n = 4, ['a', 'a', 'c', 'd'], 2
t = list(combinations(s, n))
f = sum(1 for i in t if 'a' in i)
print(f/len(t))
