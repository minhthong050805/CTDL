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


def tim_nut_giua(head):
    cham = head
    nhanh = head
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
    return cham


head = tao_danh_sach([1, 2, 3, 4, 5])
print(tim_nut_giua(head).val)
