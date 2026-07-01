class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack underflow")
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]


ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
print(ms.getMin())
ms.pop()
ms.pop()
print(ms.getMin())
