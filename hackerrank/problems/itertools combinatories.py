from itertools import combinations

n, s = input().split()
sorted_list = list(combinations(sorted(n), int(s)))
print(''.join(str(i) for i in sorted_list))

