for _ in range(int(input())):
    text = input()
    length = len(text)
    half = length // 2
    if length % 2 != 0:
        if sorted(text[:half]) == sorted(text[half+1:]):
            print('YES')
        else:
            print('NO')
    else:
        if sorted(text[:half]) == sorted(text[half:]):
            print('YES')
        else:
            print('NO')


