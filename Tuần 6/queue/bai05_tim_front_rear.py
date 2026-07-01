from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            return None
        return self.data.popleft()

    def front(self):
        if not self.data:
            return None
        return self.data[0]

    def rear(self):
        if not self.data:
            return None
        return self.data[-1]


q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print(f"front = {q.front()}")
print(f"rear = {q.rear()}")
