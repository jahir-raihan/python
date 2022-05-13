lst = [[3, 12], [-2, 5], [-4, 1]]


def check_recur(p, lst, res=0):
    if len(lst) == 0:
        return res
    else:

        point = lst[0]
        res = abs((p[0] - point[0]) + (p[1] - point[1]))

        return res + check_recur(p, lst[1:])


for i in range(len(lst)):
    res = check_recur(lst[i], lst[i+1:])
    r = 0

"""I will solve it when i understand the concept of minimum spanning tree very well"""
