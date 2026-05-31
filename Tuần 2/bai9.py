a = [1, 3, 5, 6]  # vidu
x = 4  # vidu

left, right = 0, len(a) - 1
ans = len(a)

while left <= right:
    mid = (left + right) // 2
    if a[mid] >= x:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)