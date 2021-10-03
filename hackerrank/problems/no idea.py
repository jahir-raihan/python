n, arr = input(), input().split()
A, B = set(input().split()), set(input().split())
print(sum([(i in A) - (i in B) for i in arr]))
