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


def xoa_thu_k_tu_cuoi(head, k):
    nut_gia = Nut(0)
    nut_gia.next = head
    nhanh = nut_gia
    cham = nut_gia
    for _ in range(k):
        nhanh = nhanh.next
    while nhanh.next is not None:
        nhanh = nhanh.next
        cham = cham.next
    cham.next = cham.next.next
    return nut_gia.next


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


head = tao_danh_sach([1, 2, 3, 4, 5])
head = xoa_thu_k_tu_cuoi(head, 2)
in_toan_bo(head)
