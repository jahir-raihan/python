lst = [1, 6, 7, 3, 2, 4]

start = 0
width = end = len(lst)-1
res = min(lst[start], lst[end])*width

while start < end:
    if lst[start] < lst[end]:
        start += 1
    else:
        end -= 1
    width -= 1
    res = max(res, min(lst[start], lst[end])*width)