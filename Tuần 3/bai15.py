a = [('An', 8), ('Ba', 9), ('Cu', 8)]  # //vidu

n = len(a)
for i in range(n - 1):
    for j in range(n - 1 - i):
        ten_j,   diem_j   = a[j]
        ten_j1,  diem_j1  = a[j + 1]
        if diem_j < diem_j1 or (diem_j == diem_j1 and ten_j > ten_j1):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)  
