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


def tach_doi(head):
    cham = head
    nhanh = head.next
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
    giua = cham.next
    cham.next = None
    return head, giua


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


def merge_sort(head):
    if head is None or head.next is None:
        return head
    trai, phai = tach_doi(head)
    trai = merge_sort(trai)
    phai = merge_sort(phai)
    return tron(trai, phai)


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


head = tao_danh_sach([3, 1, 2])
head = merge_sort(head)
in_toan_bo(head)
