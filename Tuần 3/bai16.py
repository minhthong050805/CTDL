a = [2, 3, 1]  # //vidu
n = len(a)
nghich_the = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            nghich_the += 1
b = a[:]
so_swap = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            so_swap += 1

print(f"Nghịch thế: {nghich_the}")  
print(f"Số swap:    {so_swap}")     
print(f"Bằng nhau:  {nghich_the == so_swap}")  
