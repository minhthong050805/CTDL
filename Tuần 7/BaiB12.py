class Nut:
    def __init__(self, val):
        self.val = val
        self.next = None


def tim_diem_bat_dau_chu_trinh(head):
    cham = head
    nhanh = head
    co_chu_trinh = False
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
        if cham == nhanh:
            co_chu_trinh = True
            break
    if not co_chu_trinh:
        return None
    cham = head
    while cham != nhanh:
        cham = cham.next
        nhanh = nhanh.next
    return cham


a = Nut(1)
b = Nut(2)
c = Nut(3)
d = Nut(4)
a.next = b
b.next = c
c.next = d
d.next = b

diem_bat_dau = tim_diem_bat_dau_chu_trinh(a)
print(diem_bat_dau.val if diem_bat_dau is not None else None)
