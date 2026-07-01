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


def chen_sau_nut(nut, val):
    nut_moi = Nut(val)
    nut_moi.next = nut.next
    nut.next = nut_moi


def chen_sau_vi_tri(head, k, val):
    nut = head
    for _ in range(k):
        nut = nut.next
    chen_sau_nut(nut, val)


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


head = tao_danh_sach([1, 3])
chen_sau_nut(head, 2)
in_toan_bo(head)
