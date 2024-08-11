s = input("Nhập một chuỗi: ")
str = {}

for char in s:
    if char in str:
        str[char] += 1
    else:
        str[char] = 1

print(str)