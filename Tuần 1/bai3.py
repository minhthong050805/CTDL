def dem_so_sanh(a, x):
    dem = 0
    for i in range(len(a)):
        dem += 1
        if a[i] == x:
            return dem, i
    return dem, -1

A = [7, 3, 9, 12, 5, 8, 1]

for x in [7, 1, 100]:
    dem, vi_tri = dem_so_sanh(A, x)
    print(f"x={x}: so phep so sanh = {dem}, vi tri = {vi_tri}")

print("Phan tu o dau mang can it phep so sanh, phan tu o cuoi hoac khong ton tai can nhieu phep so sanh hon")
