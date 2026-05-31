a = [4, 5, 6, 7, 0, 1, 2]  # vidu
x = 0  # vidu

left, right = 0, len(a) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        ans = mid
        break

    if a[left] <= a[mid]:
        if a[left] <= x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if a[mid] < x <= a[right]:
            left = mid + 1
        else:
            right = mid - 1

print(ans)