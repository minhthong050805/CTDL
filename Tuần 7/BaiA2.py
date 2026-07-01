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

    def popBack(self):
        if self.n == 0:
            raise IndexError("Danh sach rong")
        self.n -= 1
        return self.data[self.n]

    def to_list(self):
        return [self.data[i] for i in range(self.n)]


ds = MangDong()
ds.append(1)
ds.append(2)
ds.append(3)
gia_tri = ds.popBack()
print("Sau popBack:", ds.to_list(), ", gia tri xoa:", gia_tri)
