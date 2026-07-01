class PriorityQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, value, priority):
        self.data.append((priority, value))
        self.data.sort(key=lambda x: x[0], reverse=True)

    def dequeue(self):
        if not self.data:
            raise IndexError("Queue rong")
        return self.data.pop(0)[1]

    def peek(self):
        if not self.data:
            raise IndexError("Queue rong")
        return self.data[0][1]

    def isEmpty(self):
        return len(self.data) == 0


pq = PriorityQueue()
pq.enqueue("task_low", 1)
pq.enqueue("task_high", 5)
pq.enqueue("task_medium", 3)
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
