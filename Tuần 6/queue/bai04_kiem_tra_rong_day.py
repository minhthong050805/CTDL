class QueueCoGioi:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def enqueue(self, value):
        if len(self.data) >= self.capacity:
            print("Loi: Queue day")
            return
        self.data.append(value)
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.isEmpty():
            print("Loi: Queue rong")
            return None
        val = self.data.pop(0)
        print(f"Dequeued {val}")
        return val

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) >= self.capacity

    def count(self):
        return len(self.data)


q = QueueCoGioi(3)
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(f"So phan tu: {q.count()}")
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
