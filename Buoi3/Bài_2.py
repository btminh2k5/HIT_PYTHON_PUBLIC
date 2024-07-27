s1 = input()
s2= input()

# 1: In ra đảo ngược của chuỗi s1
for i in range(-1, -len(s1) - 1, -1):
    print(s1[i], end = "")
print("")

#2: Nhập vào 2 số nguyên a, b (1 <=a < b <= len(s2)). In ra 
# chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
a = int(input())
b = int(input())
tmp = []
if 0 <= a < b < len(s2):
    tmp = s2[a:b + 1][::-1]
tmp2 = s2[:a] + tmp + s2[b + 1:]
print(tmp2)

#3: In ra chuỗi s3 là chuỗi s1 sau khi 
# xóa các kí tự vị trí chẵn
s3 = s1[0::2]
print(s3)

#4: Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
s4 = ""
tmp2 = len(s1) if len(s1) < len(s2) else len(s2)
for i in range(tmp2):
    s4 += s1[i] + s2[i]
if len(s2) - tmp2 > 0:
    print(s4 + s2[tmp2::])
else:
    print(s4 + s1[tmp2::])
#4 : Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
print(s1[0] + s2[1::])
print(s2[0] + s1[1::])