from itertools import *


def find_min(X, res=81):
    for i in permutations(range(1, 10)):
        if sum(i[0:3]) == 15 and sum(i[3:6]) == 15 and sum(i[0::3]) == 15 and sum(i[1::3]) == 15 and i[0] + i[4] + i[8] == 15 and (i[2] + i[4] + i[6] == 15):
            res = min(res, sum(abs(i[p] - X[p]) for p in range(0, 9)))
    return res


X = []
for _ in range(3):
    X.extend(list(map(int, input().split())))
print(find_min(X))


