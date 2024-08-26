def sum_numbers_in_string(s):
    total, num = 0, ''
    for char in s:
        if char.isdigit() or (char == '-' and num == ''):
            num += char
        elif num:
            total += int(num)
            num = ''
    if num:
        total += int(num)
    return total
s = input("Nhập chuỗi ký tự: ")
result = sum_numbers_in_string(s)
print("Tổng các số trong chuỗi là:", result)
