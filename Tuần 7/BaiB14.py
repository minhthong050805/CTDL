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


def cong_hai_so(a, b):
    nut_gia = Nut(0)
    nut = nut_gia
    nho = 0
    while a is not None or b is not None or nho != 0:
        gia_tri_a = a.val if a is not None else 0
        gia_tri_b = b.val if b is not None else 0
        tong = gia_tri_a + gia_tri_b + nho
        nho = tong // 10
        nut.next = Nut(tong % 10)
        nut = nut.next
        if a is not None:
            a = a.next
        if b is not None:
            b = b.next
    return nut_gia.next


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


a = tao_danh_sach([2, 4, 3])
b = tao_danh_sach([5, 6, 4])
in_toan_bo(cong_hai_so(a, b))
