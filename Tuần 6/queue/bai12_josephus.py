from collections import deque


def josephus(n, k):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()
    return q[0]


print(josephus(5, 2))
print(josephus(7, 3))
