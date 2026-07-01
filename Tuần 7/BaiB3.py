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


def tim_kiem(head, x):
    vi_tri = 0
    nut = head
    while nut is not None:
        if nut.val == x:
            return vi_tri
        nut = nut.next
        vi_tri += 1
    return -1


head = tao_danh_sach([1, 2, 3])
print(tim_kiem(head, 2))
