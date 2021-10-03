for t in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    l, i = len(lst), 0
    while i < l - 1 and lst[i] >= lst[i+1]:i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:i += 1
    print("Yes" if i == l - 1 else "No")