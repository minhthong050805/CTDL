a = [1, 3, 5, 7]  # vidu
x = 4  # vidu

n = len(a)
left, right = 0, n - 1
ans = n

while left <= right:
    mid = (left + right) // 2
    if a[mid] >= x:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)