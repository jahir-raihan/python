s = []
cur = tree.root
while True:
    if cur:
        s.insert(0, cur)
        cur = cur.left
    elif s:
        val = s.pop(0)
        print(val.info, end=' ')
        cur = val.right
    else:
        break
