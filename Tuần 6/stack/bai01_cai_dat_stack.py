class Stack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = []

    def push(self, value):
        if len(self.data) >= self.capacity:
            raise OverflowError("Stack overflow")
        self.data.append(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack underflow")
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.top())
print(s.isEmpty())
