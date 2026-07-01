def tron_khoang(khoang):
    khoang = sorted(khoang, key=lambda x: x[0])
    ket_qua = []
    for kv in khoang:
        if len(ket_qua) == 0 or ket_qua[-1][1] < kv[0]:
            ket_qua.append(list(kv))
        else:
            ket_qua[-1][1] = max(ket_qua[-1][1], kv[1])
    return ket_qua


khoang = [[1, 3], [2, 6], [8, 10]]
print(tron_khoang(khoang))
