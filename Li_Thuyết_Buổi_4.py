# TUPLE
# Gần tương tự như list: có thể chứa các phần tử khác kiểu dữ liệu
# Không giống như list, bộ giá trị của tuple là bất biến. Không thể được thay đổi sau khi gán.
# Tuy nhiên, nếu bản thân phần tử trong tuple là một kiểu dữ liệu khả biến (vd list),
# thì các giá trị bên trong phần tử đó có thể được thay đổi.  

# # tuple rỗng
# t0 = ()
# # tuple chứa item có khác kiểu dữ liệu
# t1 =(1, "Hello", 34)
# # khởi tạo không dùng ()
# t2 = 1, 2, "Hello"
# # tuple lồng nhau
# t3 =(1, (2, 'HIT'), 4)
# print(f"t0 = {t0} \t({type(t0)})")
# print(f"t1 = {t1} \t({type(t1)})")
# print(f"t2 = {t2} \t({type(t2)})")
# print(f"t3 = {t3} \t({type(t3)})")
# Cách thay đổi giá trị trong tuple bằng cách ép kiểu thành list
# t1 = list(t1)
# t1[1] = 'Hi'
# t1 = tuple(t1)
# print(t1)


# set(tập hợp)
# Set là một tập hợp không có chỉ số, nên không truy xuất qua index được.
# Các phần tử trong một set có thể khác kiểu, nhưng set không thể chứa một set.
# Mỗi phần tử của set là duy nhất và bất biến (không thể thay đổi).
# Ta có thể thêm phần tử vào hoặc xóa phần tử từ một
# # khởi tạo set
# set = {1,2,1,4,6,3,5}
# print(set)

# # thêm item vào set
# # thêm 1 item
# set.add(10)
# print(set)
# # thêm nhiều item
# set.update([11,12,13,200,2093,72621862])
# print(set)

# xóa item ra khỏi set
# Xóa 1 item, nếu item không có trong set thì sẽ bị lỗi KeyError
# set.remove(10)
# print(set)
# # Xóa 1 item bất kỳ, và trả về giá trị của item đó
# print(set.pop())
# print(set)
# # Xóa tất cả items
# set.clear()
# print(set)
# # Xóa 1 item, nếu item không có trong set thì sẽ không làm gì
# set.discard()
# print(set)

# Các phương thức xác thực
# <set>.issubset(OtherSet)
# Kiểm tra set có phải tập con của OtherSet
# s1 = {1,2,3,4}
# print(s1)
# print(s1.issubset(set))
# <set>.issuperset(OtherSet)
#      Kiểm tra OtherSet là tập hợp con của Set
# print(s1.issuperset(set))

# Toán tử và các thao tác trên set
# s = {'blue','green','red'}
# s1 = {'yellow', 'red', 'orange'}
# # Phép hợp: lấy tập dữ liệu của cả 2 tập hợp
# print(s | s1)
# # Phép giao: lấy tập dữ liệu trùng nhau 
# print(s & s1)
# # Phép hiệu: lấy tập dữ liệu chỉ có trong a không có trong b
# print(s - s1)
# # Phép khác biệt đối xứng: lấy tập dữ liệu không bị trùng của cả 2
# print(s ^ s1)


# Bài tập 1
# str = "Hoc lap trinh python cung HIT"
# # Cách 1: for thông thường
# result = []
# for char in str:
#     if char == " ":
#         continue
#     result.append(char)
# print("Tuple1=", tuple(result))

# # Cách 2
# result2 = []
# for index in range(len(str)):
#     if str[index] == " ":
#         continue
#     result2.append(str[index])
# print("Tuple2=",tuple(result2))
# # Cách 3: list comprehension
# result3 = (char for char in str if char is not " ")
# print("Tuple3=", tuple(result3))

# occurences_char_o = [1 for char in result if char == "o"]
# print('o occurences=', len(occurences_char_o))


s = [1,1,2,2,3,4,5,5,5,26872,3209]
s = set(s)
l = list(s)
print(l[-2])
