def tron(a, b):
    ket_qua = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ket_qua.append(a[i])
            i += 1
        else:
            ket_qua.append(b[j])
            j += 1
    while i < len(a):
        ket_qua.append(a[i])
        i += 1
    while j < len(b):
        ket_qua.append(b[j])
        j += 1
    return ket_qua


a = [1, 3, 5]
b = [2, 4]
print(tron(a, b))
