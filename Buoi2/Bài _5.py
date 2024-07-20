n = int(input())
for i in range(0, n + 1, 1):
    stri = str(i)
    tong = 0
    for j in stri:
        tong += int(j)**3
    if tong == i:
        print(i, end = " ")