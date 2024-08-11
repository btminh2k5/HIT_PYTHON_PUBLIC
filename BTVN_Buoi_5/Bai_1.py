sv = {
    "SV01": 3.2,
    "SV02": 2.8,
    "SV03": 3.5,
    "SV04": 3.1,
    "SV05": 1.9
}

cnt = 0
for i in sv:
    if sv[i] >= 3.0 and sv[i] <= 3.5:
        cnt += 1
print(cnt)

ma_sv = input()
diem = float(input())

sv[ma_sv] = diem

sv = {ma_sv: diem for ma_sv, diem in sv.items() if diem >= 2.0}

for ma_sv, diem in sv.items():
    print(ma_sv + " " + str(diem))