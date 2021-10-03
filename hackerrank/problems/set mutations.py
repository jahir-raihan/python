_ = input()
d = set(map(int, input().split()))

dic = {
    'intersection_update': lambda x: d.intersection_update(x),
    'symmetric_difference_update': lambda x: d.symmetric_difference_update(x),
    'update': lambda x: d.update(x), 'difference_update': lambda x: d.difference_update(x)
}

for _ in range(int(input())):
    op = input().split()
    n = list(map(int, input().split()))
    dic[op[0]](n)

print(sum(d))