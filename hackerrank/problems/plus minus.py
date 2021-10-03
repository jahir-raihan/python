def plusMinus(arr, n):
    pos = neg = zero = 0
    for i in arr:
        if i < 0:
            neg += 1
            continue
        if i == 0:
            zero += 1
            continue
        else:
            pos += 1
    print(f'{(pos / n):{6}f}')
    print(f'{(neg / n):{6}f}')
    print(f'{(zero/n):{6}f}')


n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr, n)