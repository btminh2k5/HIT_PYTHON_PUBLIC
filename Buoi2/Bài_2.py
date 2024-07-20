a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
# a)
print(f'{a} + {b} =', a + b)
# b)
print(f'{a} - {b} =', a - b)
# c)
print(f'{a} * {b} =', a * b)
# d) chia lấy nguyên
print(f'{a} // {b} =', a // b)
# e) mũ
print(f'{a} ** {b} =', a ** b)
# f) chia dư
print(f'{a} % {b} =', a % b)
# g) so sánh
if a > b:
    print(f'{a} > {b}')
elif a < b:
    print(f'{a} < {b}')
elif a == b:
    print(f'{a} = {b}')
# h) and
print(f"{a} & {b} =", a & b)
# i) or
print(f'{a} | {b} =', a | b)
# j) xor
print(f'{a} ^ {b} =', a ^ b)
# k) not
print(a is not b)
# l)
print(a >> a)
# m)
print(a << a)