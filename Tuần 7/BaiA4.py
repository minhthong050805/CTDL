def indexOf(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


a = [5, 3, 7]
print(indexOf(a, 7))
print(indexOf(a, 100))
