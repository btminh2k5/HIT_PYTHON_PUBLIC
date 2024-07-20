n = int(input())
a = 0
b = 1
tong = 0
print("0" + " 1", end = " ")
for i in range(2, n, 1):
    tong = a + b
    print(tong, end = " ")
    a = b
    b = tong