class MangDong:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.n = 0
        self.data = [None] * capacity

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def add(self, x):
        if self.n == self.capacity:
            print(f"Day o cap {self.capacity}, cap phat cap {self.capacity * 2}")
            self.resize(self.capacity * 2)
        self.data[self.n] = x
        self.n += 1


ds = MangDong(4)
for x in [10, 20, 30, 40, 50]:
    ds.add(x)
print("Capacity cuoi cung:", ds.capacity)
print("So phan tu:", ds.n)
