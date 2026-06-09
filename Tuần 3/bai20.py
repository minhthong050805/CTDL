def dem_nghich_the(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    trai, inv_trai = dem_nghich_the(arr[:mid])
    phai, inv_phai = dem_nghich_the(arr[mid:])
    merged = []
    inv = inv_trai + inv_phai
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            merged.append(trai[i])
            i += 1
        else:
            merged.append(phai[j])
            inv += len(trai) - i  
            j += 1
    merged.extend(trai[i:])
    merged.extend(phai[j:])
    return merged, inv

import random
random.seed(42)
a = random.sample(range(1, 10**5 + 1), 10**5)  # //vidu 

_, tong_swap = dem_nghich_the(a)
print(f"Số swap (nghịch thế): {tong_swap}")
