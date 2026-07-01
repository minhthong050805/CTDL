def min_max(a):
    min_val = a[0]
    max_val = a[0]
    vi_tri_min = 0
    vi_tri_max = 0
    for i in range(1, len(a)):
        if a[i] < min_val:
            min_val = a[i]
            vi_tri_min = i
        if a[i] > max_val:
            max_val = a[i]
            vi_tri_max = i
    return min_val, vi_tri_min, max_val, vi_tri_max

a = [7, 3, 9, 12, 5, 8, 1]
min_val, vi_tri_min, max_val, vi_tri_max = min_max(a)
print("Gia tri nho nhat:", min_val, "tai vi tri:", vi_tri_min)
print("Gia tri lon nhat:", max_val, "tai vi tri:", vi_tri_max)
