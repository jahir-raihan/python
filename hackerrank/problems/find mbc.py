import math
a = int(input())
b = int(input())
tan = math.atan2(a, b)
degree = int(round(math.degrees(tan)))
print(degree)