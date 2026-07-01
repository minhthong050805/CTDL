def tim_tat_ca(a, x):
    vi_tri = []
    for i in range(len(a)):
        if a[i] == x:
            vi_tri.append(i)
    return vi_tri

a = [4, 1, 4, 9, 4]
x = 4
print(tim_tat_ca(a, x))
