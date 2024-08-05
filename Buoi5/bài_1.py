s = input()
lst = s.split()
s = set(lst)
lst_tmp = list(s)
lst_r = []
for i in lst_tmp:
    count = 0
    for j in lst:
        if j == i:
            count += 1
    if count % 5 == 0 and count % 10 != 0:
        lst_r.append(int(i))
for i in range(len(lst_r)):
    print(lst_r[i], end=' ')


