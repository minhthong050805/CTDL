def tim_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1

a = [3, 7, 11, 8, 5, 4]
print(tim_chan_dau_tien(a))
