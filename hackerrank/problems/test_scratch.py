def pattern(n):
    k = 2 * n - 2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k -= 2
        for j in range(i + 1):
            print("# ", end="")
        print("\r")


pattern(int(input()))
