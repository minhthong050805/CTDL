from collections import deque


class StackFromQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        self.q1.append(value)

    def pop(self):
        if not self.q1 and not self.q2:
            raise IndexError("Stack underflow")
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        if not self.q1 and not self.q2:
            raise IndexError("Stack is empty")
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def isEmpty(self):
        return not self.q1 and not self.q2


s = StackFromQueues()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.top())
print(s.pop())
print(s.isEmpty())
