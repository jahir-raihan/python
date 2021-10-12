number = int(input())
if number % 5 == 0 and number % 11 == 0:
    print('BOTH')
elif number % 5 == 0 or number % 11 == 0:
    print('ONE')
else:
    print('NONE')