def vi_tri_cuoi(a, x):
    ket_qua = -1
    for i in range(len(a)):
        if a[i] == x:
            ket_qua = i
    return ket_qua

a = [4, 1, 4, 9, 4]
x = 4
print(vi_tri_cuoi(a, x))
