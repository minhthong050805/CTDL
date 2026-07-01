class Nut:
    def __init__(self, val):
        self.val = val
        self.next = None


def tao_danh_sach(gia_tri):
    head = None
    tail = None
    for v in gia_tri:
        nut_moi = Nut(v)
        if head is None:
            head = nut_moi
            tail = nut_moi
        else:
            tail.next = nut_moi
            tail = nut_moi
    return head


def tron(a, b):
    nut_gia = Nut(0)
    nut = nut_gia
    while a is not None and b is not None:
        if a.val <= b.val:
            nut.next = a
            a = a.next
        else:
            nut.next = b
            b = b.next
        nut = nut.next
    nut.next = a if a is not None else b
    return nut_gia.next


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


a = tao_danh_sach([1, 3, 5])
b = tao_danh_sach([2, 4])
in_toan_bo(tron(a, b))
