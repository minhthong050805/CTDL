def gan_nhat(a, x):
    vi_tri = 0
    chenh_lech_nho_nhat = abs(a[0] - x)
    for i in range(1, len(a)):
        chenh_lech = abs(a[i] - x)
        if chenh_lech < chenh_lech_nho_nhat:
            chenh_lech_nho_nhat = chenh_lech
            vi_tri = i
    return a[vi_tri], vi_tri

a = [10, 22, 28, 29, 40]
x = 26
gia_tri, vi_tri = gan_nhat(a, x)
print("Gia tri gan nhat:", gia_tri, "tai vi tri:", vi_tri)
