n = int(input('Nhập n: '))
sum = 0
# a)
for i in range(1, 2*n+2):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print("Tổng S1 =", sum)
# b)
s = 0
for i in range(1, n + 1):
    s += 1/i
print("Tổng S2 =", s)
# c)
import math
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))

if a == 0:
    if b == 0:
        if c == 0:
            print('Phương trình vô số nghiệm')
        else:
            print('Phương trình vô nghiệm')
    else:
        print('Phương trình có nghiệm: x =', -c/b)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print('Phương trình vô nghiệm')
    elif delta == 0:
        print('Phương trình có nghiệm kép: x =', -b/(2*a))
    else:
        print("Phương trình có 2 nghiệm phân biệt:")
        print('x1 = ', (-b + math.sqrt(delta)) / (2*a))
        print('x2 = ', (-b - math.sqrt(delta)) / (2*a))