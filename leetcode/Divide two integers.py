def divide(dividend, divisor):

    sign = (-1 if ((dividend < 0) ^
                   (divisor < 0)) else 1)

    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    res = sign * quotient
    if res <= -2147483647:
        return -2**31
    if res >= 2**31 - 1:
        return 2**31 - 1
    return res

