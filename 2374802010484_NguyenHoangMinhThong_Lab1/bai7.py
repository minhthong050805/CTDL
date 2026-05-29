def tontai(a, x):
    for i in a:
        if i == x:
            return True
    return False

a = [1, 2, 3, 4, 5]
x = 3

print(tontai(a, x))