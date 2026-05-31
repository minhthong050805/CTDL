p = [12, 34, 67, 90]  # vidu
m = 2  # vidu

if m > len(p):
    ans = -1
else:
    left, right = max(p), sum(p)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        students = 1
        current_pages = 0
        for pages in p:
            if current_pages + pages > mid:
                students += 1
                current_pages = pages
            else:
                current_pages += pages

        if students <= m:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

print(ans)