for _ in range(int(input())):
    _ = input()
    A = set(map(int, input().split()))
    _ = input()
    B = set(map(int, input().split()))
    print(A.issubset(B))