pushed = [0,2,1]

popped =[0,1,2]
stk = {}

i = 0
j = len(pushed)
while j > 0:
    if pushed[i] in stk and popped[0] in stk and pushed[i] != popped[0]:
        break
    elif pushed[i] != popped[0]:
        stk[pushed[i]] = True
        i += 1
    else:
        pushed.remove(pushed[i])
        popped.pop(0)
        j -= 1
        if i != 0:
            i -= 1

