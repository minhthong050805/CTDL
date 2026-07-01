def tim_max(a):
    max_val = a[0]
    vi_tri = 0
    for i in range(1, len(a)):
        if a[i] > max_val:
            max_val = a[i]
            vi_tri = i
    return max_val, vi_tri

a = [7, 3, 9, 12, 5, 8, 1]
max_val, vi_tri = tim_max(a)
print("Gia tri lon nhat:", max_val, "tai vi tri:", vi_tri)
