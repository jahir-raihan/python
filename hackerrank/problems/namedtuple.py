from collections import namedtuple
n, Student, res = int(input()), namedtuple('Student', input()), 0
for _ in range(n):
    student = Student(*input().split())
    res += int(student.MARKS)
print(f'{res/n:.2f}')




