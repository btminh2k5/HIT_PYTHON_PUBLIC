n = int(input())

def check(number):
    tong = 0
    for j in range(1, number, 1):
        if number % j == 0:
            tong += j
    return tong

c = 2
for i in range(1, n, 1):
    tmp = check(i)
    if(tmp < n and check(tmp) == i):
        if tmp != i:
            print(i, end = " ")
            c -= 1
    if c == 0:
        print()
        c = 2