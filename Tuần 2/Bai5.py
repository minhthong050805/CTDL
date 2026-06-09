a = [1, 2, 2, 2, 3]  # vidu
x = 2  # vidu

left, right = 0, len(a) - 1
first = -1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        first = mid
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

left, right = 0, len(a) - 1
last = -1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        last = mid
        left = mid + 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

ans = 0 if first == -1 else (last - first + 1)
print(ans)