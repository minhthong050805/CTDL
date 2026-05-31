x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # vidu
k = 9  # vidu

left, right = 0.0, float(x[-1] - x[0])

while right - left > 1e-6:
    mid = (left + right) / 2.0
    count = 0
    for i in range(len(x) - 1):
        count += int((x[i + 1] - x[i]) / mid)

    if count <= k:
        right = mid
    else:
        left = mid

print(round(right, 1))