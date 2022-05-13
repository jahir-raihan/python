num = 120
if num < 0:
    temp = str(num)[:1]
    n = str(num)[1:]
    num = int(temp + n[::-1])
else:
    num = int(str(num)[::-1])
if abs(num) < 2**31 and num != 2**31 - 1:

    print(num)
else:
   print(0)
