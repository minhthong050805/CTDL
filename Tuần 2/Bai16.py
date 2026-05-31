piles = [3, 6, 7, 11]  # vidu
h = 8  # vidu

left, right = 1, max(piles)
ans = right

while left <= right:
    mid = (left + right) // 2
    hours = 0
    for p in piles:
        hours += (p + mid - 1) // mid

    if hours <= h:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)