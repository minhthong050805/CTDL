def loai_trung_on2(a):
    ket_qua = []
    for i in range(len(a)):
        da_co = False
        for j in range(len(ket_qua)):
            if ket_qua[j] == a[i]:
                da_co = True
                break
        if not da_co:
            ket_qua.append(a[i])
    return ket_qua


def loai_trung_on(a):
    da_thay = set()
    ket_qua = []
    for i in range(len(a)):
        if a[i] not in da_thay:
            da_thay.add(a[i])
            ket_qua.append(a[i])
    return ket_qua


a = [3, 1, 3, 2, 1]
print("Cach O(n^2):", loai_trung_on2(a))
print("Cach O(n):", loai_trung_on(a))
