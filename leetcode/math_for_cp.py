import time
start1 = time.time()


def power(a, b):
    if b == 0:
        return 1
    x = power(a, b//2)
    if b % 2 == 0:
        return x * x
    else:
        return x * x * a


print(power(3, 2555))
print("time took for first one :", (time.time() - start1) / 1000)
#   Alternative and faster one

start2 = time.time()


def power2(a, b):
    ans = 1

    while b > 0:
        if b % 2 == 1:
            ans = ans * a

        b = b >> 1
        a = a * a
    return ans

import math


print(power2(3, 2555))
print('Time took for second one :', (time.time() - start2) / 1000)