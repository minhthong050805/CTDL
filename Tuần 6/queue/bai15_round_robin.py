from collections import deque


def round_robin(processes, quantum):
    queue = deque()
    for pid, burst in processes:
        queue.append([pid, burst])

    time = 0
    completion = {}

    while queue:
        pid, remaining = queue.popleft()
        run = min(quantum, remaining)
        time += run
        remaining -= run
        if remaining > 0:
            queue.append([pid, remaining])
        else:
            completion[pid] = time

    print(f"{'Process':<10} {'Completion Time':<15}")
    for pid, t in sorted(completion.items()):
        print(f"{pid:<10} {t:<15}")


processes = [("P1", 5), ("P2", 3), ("P3", 8), ("P4", 2)]
round_robin(processes, quantum=2)
