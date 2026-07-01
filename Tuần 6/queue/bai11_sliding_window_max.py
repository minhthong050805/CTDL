from collections import deque


def sliding_window_max(arr, k):
    dq = deque()
    result = []
    for i in range(len(arr)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result


print(sliding_window_max([1, 3, -1, -3, 5, 3], 3))
print(sliding_window_max([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
