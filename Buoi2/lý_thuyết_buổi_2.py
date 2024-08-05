# l = [1,2,3](khai báo nhiều kiểu dữ liệu trên 1 biến) (kiểu list: có thể thay đổi được)
# print(type(l))

# t = (1,2,3) (khai báo kiểu tuple: không thể thay đổi)
# print(type(t))


# kiểu dictionary 
# my_dict = {
#     "ten" : "Minh",
#     "gioi tinh" : "Nam",
#     "Nam sinh" : 2002
# }
# d = {} (rút gọn tên biến)
# print(my_dict)
# print(type(d))

# for i in range(5):
#     print(i, end=' ')

# cách sử dụng print
# cách 1
# a = 10
# b = 6
# print('{} {}'.format(a,b) , a + b)
# cách 2
# các phép toán
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b}')
# print(f'{a} % {b} = {a % b}') # chia lấy dư
# print(f'{a} ** {b} = {a ** b}') # tính số mũ
# print(f'{a} // {b} = {a // b}') # phép chia lấy phần nguyên

# Toán tử so sánh ( ==, !=, > , < , >= , <= )
# Toán tử logic (and, or, not)
# x = 5
# print(x < 6 and x > 7)
# print(x < 6 or x > 8)
# print(not(x < 6 and x > 8))

# toán tử thành viên
# a = 1
# x = [1,2,3]
# print(a in x)

# toán tử nhận dạng "is"
# a = 5
# b = 5
# c = 1
# print(a is b)
# print(a is c)
# ngược lại là "is not"

# Toán tử bitwise 
# dịch chuyển bit << (qua trái), >> (qua phải)

# if else trong python
# if 5 < 4:
#     print("Yes")
# else:
#     print("No")
# bài tập nhập 3 số a,b,c. In ra xem 3 số đó có thành tam giác không
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     print("Yes")
# else:
#     print("No")

# a = int(input())
# if a > 20 :
#     print(a)
# elif a > 5 and a < 15:
#     print(a * a)
# else:
#     print(a - a)

# Toán tử 3 ngôi
# a = int(input())
# res = a if a < 10 else a**2
# print(res)

# print(bool(6))

# Vòng lặp for
# for i in range(1, 6, 1): #(start, stop(trước số stop), step)
#     print(i, end=' ')
# l = [1,2,3,4]
# print()
# for i in l:
#     print(i, end=' ')

# vòng lặp while
# a = 10
# while a > -5:
#     print(a, end=' ')
#     a -= 1
#     pass  #bỏ qua lệnh hoặc là "..."
#     break #dừng lệnh
#     continue #bỏ qua lệnh dưới và chạy lại lệnh trên
#     print(".....")

# hàm enumerate
# a = ["eat", "sleep", "repeat "]
# for inx, val in enumerate(a):
#     print(inx, val)

