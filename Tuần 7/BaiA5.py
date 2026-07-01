def duyet_in(a):
    for i in range(len(a)):
        print(a[i])


def dem_dieu_kien(a, dieu_kien):
    dem = 0
    for i in range(len(a)):
        if dieu_kien(a[i]):
            dem += 1
    return dem


a = [1, 2, 3, 4]
duyet_in(a)
print("So chan:", dem_dieu_kien(a, lambda x: x % 2 == 0))
