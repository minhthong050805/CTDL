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


def xoa_theo_gia_tri(head, x):
    if head is None:
        return None
    if head.val == x:
        return head.next
    nut = head
    while nut.next is not None:
        if nut.next.val == x:
            nut.next = nut.next.next
            return head
        nut = nut.next
    return head


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


head = tao_danh_sach([1, 2, 3, 2])
head = xoa_theo_gia_tri(head, 2)
in_toan_bo(head)
