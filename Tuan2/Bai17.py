w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # vidu
D = 5  # vidu

left, right = max(w), sum(w)
ans = right

while left <= right:
    mid = (left + right) // 2
    days = 1
    current_weight = 0
    for weight in w:
        if current_weight + weight > mid:
            days += 1
            current_weight = weight
        else:
            current_weight += weight

    if days <= D:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)