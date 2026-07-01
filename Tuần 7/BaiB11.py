class NutDoi:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DanhSachLienKetDoi:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, val):
        nut_moi = NutDoi(val)
        if self.head is None:
            self.head = nut_moi
            self.tail = nut_moi
        else:
            nut_moi.next = self.head
            self.head.prev = nut_moi
            self.head = nut_moi

    def pushBack(self, val):
        nut_moi = NutDoi(val)
        if self.tail is None:
            self.head = nut_moi
            self.tail = nut_moi
        else:
            nut_moi.prev = self.tail
            self.tail.next = nut_moi
            self.tail = nut_moi

    def popFront(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def popBack(self):
        if self.tail is None:
            return None
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return val

    def duyet_xuoi(self):
        nut = self.head
        ket_qua = []
        while nut is not None:
            ket_qua.append(str(nut.val))
            nut = nut.next
        print("->".join(ket_qua))

    def duyet_nguoc(self):
        nut = self.tail
        ket_qua = []
        while nut is not None:
            ket_qua.append(str(nut.val))
            nut = nut.prev
        print("->".join(ket_qua))


ds = DanhSachLienKetDoi()
ds.pushBack(1)
ds.pushBack(2)
ds.pushFront(0)
ds.duyet_xuoi()
ds.duyet_nguoc()
