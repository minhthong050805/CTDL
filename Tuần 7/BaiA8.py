def removeIf(a, dieu_kien):
    ghi = 0
    for doc in range(len(a)):
        if not dieu_kien(a[doc]):
            a[ghi] = a[doc]
            ghi += 1
    del a[ghi:]
    return a


a = [1, 2, 3, 4]
removeIf(a, lambda x: x % 2 == 0)
print(a)
