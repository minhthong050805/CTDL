a = [2, 4, 6, 8]  # vidu
x = 5  # vidu

left, right = 0, len(a) - 1
ans = False

while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        ans = True
        break
    elif a[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

print(ans)