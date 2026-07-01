class MangDong:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.n = 0
        self.data = [None] * capacity

    def size(self):
        return self.n

    def add(self, x):
        if self.n == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.n):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.n] = x
        self.n += 1

    def get(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("Chi so ngoai pham vi")
        return self.data[i]

    def set(self, i, val):
        if i < 0 or i >= self.n:
            raise IndexError("Chi so ngoai pham vi")
        self.data[i] = val


ds = MangDong()
ds.add(1)
ds.add(2)
ds.add(3)
print("get(1) =", ds.get(1))
ds.set(1, 20)
print("Sau khi set(1, 20):", [ds.get(i) for i in range(ds.size())])
print("size =", ds.size())
