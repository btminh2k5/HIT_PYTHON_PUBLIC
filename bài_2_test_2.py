def so_hoan_hao(k):
    count = 0
    num = 19  
    while True:
        if sum(int(digit) for digit in str(num)) == 10:
            count += 1
            if count == k:
                return num
        num += 9
k = int(input("Nhập giá trị k: "))
result = so_hoan_hao(k)
print(result)