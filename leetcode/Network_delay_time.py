dic = {}

times = [[1,2,1],[2,3,2],[1,3,2]]
for i in times:
    if i[0] in dic:
        dic[i[0]].append((i[1], i[2]))

    else:
        dic[i[0]] = [(i[1], i[2])]


def find(item, target, time=1):

    for i in item:
        if i[0] == target:

            return [i[1], True]

        elif i[0] in dic:
            tmp = find(dic[i[0]], target=target)
            if tmp[1]:
                time = time + tmp[0]

                return [time, tmp[1]]

        else:
            continue
    return [time, False]


var = find(dic[1], 3)
