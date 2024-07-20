n = int(input())

def check(number):
    tong = 0
    for j in range(1, number, 1):
        if number % j == 0:
            tong += j
    if tong == number:
        return True
    else:
        return False

for i in range(1, n, 1):
    if check(i):
        print(i, end = " ")