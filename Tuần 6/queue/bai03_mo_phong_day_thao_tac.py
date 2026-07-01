from collections import deque


def mo_phong_queue(lenh):
    q = deque()
    for cmd in lenh:
        if cmd[0] == "enqueue":
            q.append(cmd[1])
        elif cmd[0] == "dequeue":
            if q:
                print(f"dequeue -> {q.popleft()}")
            else:
                print("dequeue -> Queue rong")
    print(f"Trang thai cuoi: {list(q)}")


lenh = [("enqueue", 5), ("enqueue", 7), ("dequeue",), ("enqueue", 3), ("dequeue",)]
mo_phong_queue(lenh)
