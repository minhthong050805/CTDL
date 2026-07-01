class Nut:
    def __init__(self, val):
        self.val = val
        self.next = None


class DanhSachLienKet:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, val):
        nut_moi = Nut(val)
        nut_moi.next = self.head
        self.head = nut_moi
        if self.tail is None:
            self.tail = nut_moi

    def pushBack(self, val):
        nut_moi = Nut(val)
        if self.tail is None:
            self.head = nut_moi
            self.tail = nut_moi
        else:
            self.tail.next = nut_moi
            self.tail = nut_moi

    def in_toan_bo(self):
        nut = self.head
        ket_qua = []
        while nut is not None:
            ket_qua.append(str(nut.val))
            nut = nut.next
        print("->".join(ket_qua) + "->null")


ds = DanhSachLienKet()
ds.pushFront(2)
ds.pushBack(5)
ds.in_toan_bo()
