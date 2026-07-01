class MaTranDong:
    def __init__(self):
        self.data = []

    def them_hang(self, so_cot=0):
        self.data.append([None] * so_cot)

    def them_cot(self):
        for hang in self.data:
            hang.append(None)

    def set(self, i, j, val):
        self.data[i][j] = val

    def get(self, i, j):
        return self.data[i][j]


mt = MaTranDong()
mt.them_hang(3)
mt.them_hang(3)
mt.set(0, 0, 5)
mt.set(1, 2, 9)
print("get(0,0) =", mt.get(0, 0))
print("get(1,2) =", mt.get(1, 2))
mt.them_cot()
print("Sau khi them cot:", mt.data)
