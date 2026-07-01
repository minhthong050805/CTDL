class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.isFull():
            print("Queue day")
            return
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue rong")
            return None
        val = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return val

    def front(self):
        if self.isEmpty():
            return None
        return self.data[self.head]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


cq = CircularQueue(4)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(5)
cq.enqueue(6)
print(cq.front())
