class MangDong:
    def __init__(self):
        self.data = []
        self.modCount = 0

    def add(self, x):
        self.data.append(x)
        self.modCount += 1

    def remove_at(self, i):
        del self.data[i]
        self.modCount += 1

    def iterator(self):
        return DanhSachIterator(self)


class DanhSachIterator:
    def __init__(self, ds):
        self.ds = ds
        self.vi_tri = 0
        self.modCount_ban_dau = ds.modCount

    def has_next(self):
        return self.vi_tri < len(self.ds.data)

    def next(self):
        if self.ds.modCount != self.modCount_ban_dau:
            raise RuntimeError("ConcurrentModificationException: danh sach da bi thay doi")
        val = self.ds.data[self.vi_tri]
        self.vi_tri += 1
        return val


ds = MangDong()
for x in [1, 2, 3]:
    ds.add(x)

it = ds.iterator()
print(it.next())
ds.add(4)
try:
    print(it.next())
except RuntimeError as loi:
    print("Loi:", loi)
