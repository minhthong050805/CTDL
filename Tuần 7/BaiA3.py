class MangDong:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.n = 0
        self.data = [None] * capacity

    def size(self):
        return self.n

    def append(self, x):
        if self.n == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.n):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.n] = x
        self.n += 1

    def insert(self, i, val):
        if i < 0 or i > self.n:
            raise IndexError("Chi so ngoai pham vi")
        self.append(None)
        for j in range(self.n - 1, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = val

    def remove(self, i):
        if i < 0 or i >= self.n:
            raise IndexError("Chi so ngoai pham vi")
        val = self.data[i]
        for j in range(i, self.n - 1):
            self.data[j] = self.data[j + 1]
        self.n -= 1
        return val

    def to_list(self):
        return [self.data[i] for i in range(self.n)]


ds = MangDong()
for x in [1, 2, 4]:
    ds.append(x)
ds.insert(2, 3)
print("Sau chen 3 tai idx 2:", ds.to_list())
ds.remove(0)
print("Sau xoa idx 0:", ds.to_list())
