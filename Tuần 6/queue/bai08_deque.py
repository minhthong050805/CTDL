from collections import deque


class Deque:
    def __init__(self):
        self.data = deque()

    def pushFront(self, value):
        self.data.appendleft(value)

    def pushBack(self, value):
        self.data.append(value)

    def popFront(self):
        if not self.data:
            raise IndexError("Deque rong")
        return self.data.popleft()

    def popBack(self):
        if not self.data:
            raise IndexError("Deque rong")
        return self.data.pop()

    def peekFront(self):
        return self.data[0]

    def peekBack(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(list(self.data))


dq = Deque()
dq.pushFront(1)
dq.pushBack(2)
dq.pushFront(0)
print(dq)
print(dq.popFront())
print(dq.popBack())
print(dq)
