# a)
n = int(input("Nhập số dương: "))

sum = 0
for i in range(0, n + 1):
    sum += i
print("Tổng của các chữ số là:",sum)

# b)
n = int(input('Nhập số nguyên dương: '))
sum = 0
print("Các ước của", n, "là:", end=' ')
for i in range(1, n + 1, 1):
    if n % i == 0:
        sum += i
        print(i, end=' ')
print("và tổng của chung là:", sum)

# c) 
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều")
    elif (a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b) and (a == b or b == c or a == c): 
        print("Đây là tam giác vuông cân")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân")
    elif a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b:
        print("Đây là tam giác vuông")
    elif (a ** 2 + b ** 2 > c ** 2) and (a ** 2 + c ** 2 > b ** 2) and (b ** 2 + c ** 2 > a ** 2):
        print("Đây là tam giác nhọn")
    else:
        print("Đây là tam giác tù")
else:
    print("Không tạo thành tam giác")