def dao_nguoc(a):
    trai, phai = 0, len(a) - 1
    while trai < phai:
        a[trai], a[phai] = a[phai], a[trai]
        trai += 1
        phai -= 1
    return a


a = [1, 2, 3, 4]
dao_nguoc(a)
print(a)
