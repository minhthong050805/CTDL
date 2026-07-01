def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False

a = [3, 6, 1, 9, 4]
print(ton_tai(a, 9))
print(ton_tai(a, 100))
