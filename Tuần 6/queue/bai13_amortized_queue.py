class QueueAmortized:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.total_ops = 0
        self.total_cost = 0

    def enqueue(self, value):
        self.in_stack.append(value)
        self.total_ops += 1
        self.total_cost += 1

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                self.total_cost += 1
        if not self.out_stack:
            raise IndexError("Queue rong")
        self.total_ops += 1
        self.total_cost += 1
        return self.out_stack.pop()

    def amortized_cost(self):
        if self.total_ops == 0:
            return 0
        return self.total_cost / self.total_ops


q = QueueAmortized()
for i in range(1, 6):
    q.enqueue(i)
for _ in range(5):
    print(q.dequeue())

print(f"Tong thao tac: {q.total_ops}")
print(f"Tong chi phi: {q.total_cost}")
print(f"Chi phi trung binh: {q.amortized_cost():.2f}")
