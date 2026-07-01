def linear_search_sentinel(a, x):
    n = len(a)
    a.append(x)
    i = 0
    dem = 0
    while a[i] != x:
        i += 1
        dem += 1
    a.pop()
    if i < n:
        return i, dem + 1
    return -1, dem + 1

def linear_search_thuong(a, x):
    dem = 0
    for i in range(len(a)):
        dem += 1
        if a[i] == x:
            return i, dem
    return -1, dem

a = [7, 3, 9, 12, 5, 8, 1]
x = 1

vi_tri_s, dem_s = linear_search_sentinel(a, x)
vi_tri_t, dem_t = linear_search_thuong(a, x)

print("Sentinel: vi tri =", vi_tri_s, ", so phep so sanh =", dem_s)
print("Thong thuong: vi tri =", vi_tri_t, ", so phep so sanh =", dem_t)
