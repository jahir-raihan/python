import math

a = int(input('Enter the value of a:'))     # Initial values
b = int(input('enter the value of b:'))     # Initial values
c = int(input('enter the value of c: '))    # Initial values

d = b * b - 4*(a*c)     # method to find out the equation
if d > 0:

    x1 = (-b + math.sqrt(d)) / 2*a
    x2 = (-b - math.sqrt(d)) / 2*a

    print('Roots are real and unequal and are:', x1, x2)
elif d == 0:
    x = -b / (2*a)
    print('Roots are real and equal and are: ', x)

else:
    print("The roots are imaginary")

