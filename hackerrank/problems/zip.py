N, X = input().split()

marks = []
for _ in range(int(3)):
    marks += [list(map(float, input().split()))]

for i in zip(*marks):
    print(sum(i)/len(i))


