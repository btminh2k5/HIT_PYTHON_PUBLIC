# 1: Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
dem = 0
x = int(input())
for i in lst:
    if i == x:
        dem += 1

print(dem)

# 2: Thay thế phần tử từ vị trí 2 -> 7 trong list thành [8, 5, 4, 0, 1, 3].
tmp = [8, 5, 4, 0, 1, 3]
lst[1:7] = tmp
print(lst)

# 3: Tìm số lớn nhất, và nhỏ nhất trong list.
print(max(lst))
print(min(lst))

# 4: Nhập một số Y tùy chọn từ bàn phím. Chèn số Y vào đầu list.
# Sau khi chèn số Y, kiểm tra các số trong list có sắp xếp theo 
# thứ tự tăng dần hay giảm dần không. Nếu sắp xếp theo tăng dần thì in ra màn hình “TĂNG”, 
# còn nếu sắp xếp theo thứ tự giảm dần thì in ra màn hình “GIÁM”, nếu không tăng không giảm thì in “NO”.

y = int(input())
lst.insert(0, y)

if lst == sorted(lst):
    print("TANG")
elif lst == sorted(lst, reverse= True):
    print("GIAM")
else:
    print("NO")

# 5: Tạo một list mới có N phần tử. Các phần tử sẽ có
#  vị trí từ 1 -> N. Với mỗi phần tử ở vị trí i (1 <= i <= N) giá trị của nó là tổng i phần tử đầu tiên của list cũ.
lst2 = []
tong = 0
for i in lst:
    tong += i
    lst2.append(tong)
print(lst2)

# 6: Tạo một list mới [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000] 
# và sắp xếp nó theo thứ tự tăng dần của giá trị, và sắp xếp nó theo sự tăng dần của giá trị tuyệt đối.

lst3 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print(sorted(lst3))
lst3_tmp = []
for i in lst3:
    lst3_tmp.append(abs(i))
print(sorted(lst3_tmp))