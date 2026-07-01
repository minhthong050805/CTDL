class StackCoGioi:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def push(self, value):
        if len(self.data) >= self.capacity:
            print("Loi: Stack overflow")
            return
        self.data.append(value)
        print(f"Pushed {value}")

    def pop(self):
        if not self.data:
            print("Loi: Stack underflow")
            return None
        val = self.data.pop()
        print(f"Popped {val}")
        return val

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) >= self.capacity


s = StackCoGioi(3)
s.pop()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.pop()
s.pop()
s.pop()
s.pop()
