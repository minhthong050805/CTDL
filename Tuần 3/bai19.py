a = [1, 2, 3, 5, 4]  # //vidu
sorted_a = sorted(a)
vi_tri_dung = {}
for i, v in enumerate(sorted_a):
    vi_tri_dung[v] = i

do_lech_max = 0
for i, v in enumerate(a):
    do_lech = i - vi_tri_dung[v]
    if do_lech > do_lech_max:
        do_lech_max = do_lech
b = a[:]
n = len(b)
so_luot = 0
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
            swapped = True
    so_luot += 1
    if not swapped:
        break

print(f"Số lượt:           {so_luot}")     
print(f"Độ lệch trái max:  {do_lech_max}")
