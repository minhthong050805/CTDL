def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):
            return a[i], i
    return -1, -1

a = [4, 6, 9, 7, 11]
gia_tri, vi_tri = tim_nguyen_to_dau_tien(a)
print("Gia tri:", gia_tri, "Vi tri:", vi_tri)
