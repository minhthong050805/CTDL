def dao_doan(a, trai, phai):
    while trai < phai:
        a[trai], a[phai] = a[phai], a[trai]
        trai += 1
        phai -= 1


def xoay_phai(a, k):
    n = len(a)
    k = k % n
    dao_doan(a, 0, n - 1)
    dao_doan(a, 0, k - 1)
    dao_doan(a, k, n - 1)
    return a


a = [1, 2, 3, 4, 5]
xoay_phai(a, 2)
print(a)
