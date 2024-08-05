s = input()
result = []
for char in s:
    if char == " ":
        continue
    result.append(char)
print(set(list(result)))