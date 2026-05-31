a = [1, 3, 5, 7, 9]  # vidu
x = 7  # vidu

n = len(a)
left, right = 0, n - 1
ans = -1

while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        ans = mid
        break
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

print(ans)