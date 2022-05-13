nums = [1, 1, 3]

from itertools import permutations

perm = permutations(nums)
print(list(list(i) for i in set(perm)))

