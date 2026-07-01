class MangDong:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.n = 0
        self.data = [None] * capacity
        self.tong_thao_tac_sao_chep = 0

    def append(self, x):
        if self.n == self.capacity:
            new_capacity = self.capacity * 2
            new_data = [None] * new_capacity
            for i in range(self.n):
                new_data[i] = self.data[i]
                self.tong_thao_tac_sao_chep += 1
            self.data = new_data
            self.capacity = new_capacity
        self.data[self.n] = x
        self.n += 1


n = 16
ds = MangDong(1)
for i in range(n):
    ds.append(i)

print("So lan append:", n)
print("Tong so thao tac sao chep khi mo rong:", ds.tong_thao_tac_sao_chep)
print("Tong thao tac (append + sao chep):", n + ds.tong_thao_tac_sao_chep)
print("Trung binh moi append:", (n + ds.tong_thao_tac_sao_chep) / n)
print("Ket luan: moi lan mo rong gap doi, tong chi phi sao chep tren n lan append la O(n)")
print("Vay chi phi trung binh (amortized) cho moi append la O(1)")
