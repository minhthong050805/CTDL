a = [1, 2, 2, 2, 3]  # vidu
x = 2  # vidu

left, right = 0, len(a) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        ans = mid
        left = mid + 1
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

print(ans)