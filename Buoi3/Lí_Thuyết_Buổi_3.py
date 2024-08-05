# Khởi tạo chuỗi string
# my_string = 'Hello'
# my_string = "Hello"
# my_string = '''Hello tất cả
# mọi người nhé!''' # sử dụng 3 dấu nháy kếp để kéo dài chuỗi thành nhiều dòng
# print(my_string)

# Chuỗi escape sequence
# \a   Phát ra một tiếng bíp
# \b    Xóa ký tự trước nó
# \n    Newline (xuống dòng)
# \t    In horizonal tab (thụt 1 tab)
# \’    In ra ‘
# \”    In ra “ 
# \\    In ra \\
# \v    In vectical tab 

# Chuỗi trần
# src = r'D:\Code\python\HIT_PYTHON_PUBLIC\Buoi3'
# print(src)

# Định dạng chuỗi
# Định dạng số nguyên
# s1 = "Hệ nhị phân của {0} được biểu diễn là {0:b}".format (12)
# # Hệ nhị phân của 12 được biểu diễn là 1100

# # Định dạng số thực
# s2 = "Biểu diễn dưới dạng mũ: {0:e}".format (1566.345)
# # Biểu diễn dưới dạng mũ: 1.566345e+03

# # Làm tròn số

# s3 = "Một phần ba: {0:.3f}".format (1/3)
# # Một phần ba: 0.333

# # Căn lề
# s4 = "|{: <10} |{: ^10}|{:>10}|".format('list', 'tuple', 'set')
# # '|list | tuple | set|'
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# Toán tử và các thao tác trên chuỗi
# String trong python hỗ trợ những toán tử như: =, +, *, [], in, not in,...
# ghép 2 xâu: + ; nhân bản sâu: *
# s1 = "HIT"
# s2 = "PYTHON"
# s = s1 + s2
# s = s1*3
# duyệt xâu
# s1 = 'HIT PYTHON'
# for letter in s1:
#     print(letter)
# for i in range(len(s1)):
#     print(s1[i])


# Truy xuất các ký tự trong 1 chuỗi
# Sử dụng (index) chỉ số bắt đầu từ số 0
# Slicing: <Chuỗi>[Vị trí bắt đầu : vị trí đứng]
# s = "HIT PYTHON"
# print(s[0 : 3 : 1]) #vị trí bắt đầu : vị trí dừng : step


# Thay đổi hoặc xóa chuỗi
# s = "HIT PYTHON"
# s = "...." # đã gán "HIT PYTHON" thành "...."
# del s #xóa chuỗi
# print(s)

# Một số phương thức xử lý chuỗi

# lower()   Trả về một chuỗi viết thường
# upper()   Trả về một chuỗi viết hoa
# split()   Phân tách chuỗi thành list
# strip()   Trả về chuỗi đã được tối giản
# join()    Nối các chuỗi lại với nhau
# len()     Trả về độ dài của chuỗi 
# find()    Tìm kiếm xâu con
# replace() Thay thế cụm ký tự
# s = "HIT PYTHON"
# s = s.lower()
# print(s)
# s1 = 'hit python'
# if s == s1:
#     print("Yes")
# else: 
#     print("No")
# print(id(s1))
# print(id(s))

# Một số phương thức xác thực chuỗi
# islower()   Kiểm tra chuỗi viết thường
# isupper()   Kiểm tra chuỗi viết hoa
# isdigit()   Kiểm tra chuỗi có phải số
# isspace()   Kiểm tra chuỗi toàn khoảng trống không

# Bài tập 1: Nhập một xâu ký tự bất kỳ từ bàn phím. Cho biết xâu vừa nhập có bao nhiêu từ(không tính dấu cách)
# s = input("Nhập chuỗi: ")
# sum = len(s.split())
# print(sum)
# Hoặc
# print(len(input().split()))

# List(Danh sách)
# l = ['abc',1,2,[4,5,6]]
# print(l)
# List Comprehension là một cú pháp cho phép tạo ra một biến dữ liệu list mới từ một list cũ hoặc vòng lặp dạng in-line
# l = [x for x in range(10)]
# print(l)
# Nhập chuỗi list từ phím
# l = [int(input()) for _ in range(10)]
# print(l)

# List Comprehension lồng nhau
# vector = [[1,2,3],[4,5,6],[7,8,9]]
# L = [num for list in vector for num in list]
# print(L)
# Hoặc
# vector = [[1,2,3],[4,5,6],[7,8,9]]
# L = []
# for list in vector:
#     for num in list:
#         L.append(num)
# print(L)

# List Comprehension với mệnh đề if
# l = [x for x in range(10) if x % 2 == 0]
# print(l)
# # Hoặc
# l = []
# for x in range(10):
#     if x % 2 == 0:
#         l.append(x)
# print(l)

# Truy xuất các phần tử trong 1 list
# l = [1,2,3,4,5]
# print(l[0:4:1]) #start : stop : step 
# print(l[::-1]) #đảo ngược chuỗi
# # sửa list
# l[1:] = [10,3,4,5] 
# # Chèn 
# l[:-3] = [10,9,8]
# # xóa 
# l[:] = []
# print(l)


# clone hoặc copy
# Khi thực hiện new_List = old_List thì không tạo ra list mới mà new_List và old_List đều tham chiếu đến cùng một list khi gán.
# l = [1,2,3,4,5]
# l1 = l.copy()
# print(l1)
# print(id(l))
# print(id(l1))

# Built-in Methods with list
# append()                Thêm 1 phần tử vào cuối list
# clear()                 Xóa tất cả các item khỏi list
# copy()                  Copy 1 list
# count(item)             Đếm số lượng item có trong list
# extend()                Thêm 1 phần tử hoặc 1 list khác vào cuối list
# index(index, start, end) Trả về vị trí của phần tử cần tìm
# insert(index,item)      Chèn item tại vị trí index vào list
# pop()                   Xóa 1 phần tử ở cuối list
# remove(item)            Xóa item đầu tiên xuất hiện trong list
# reverse()               Đảo ngược các vị trí các phần tử trong list
# sort()                  Sắp xếp list
# n = int(input())
# a = [int(input()) for _ in range(n)]
# b = [int(input()) for _ in range(n)]
# a.sort()
# print(a)
# b = b*2
# b = b[::-1]
# c = b + a
# print(c)