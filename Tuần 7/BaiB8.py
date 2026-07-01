class Nut:
    def __init__(self, val):
        self.val = val
        self.next = None


def co_chu_trinh(head):
    cham = head
    nhanh = head
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
        if cham == nhanh:
            return True
    return False


a = Nut(1)
b = Nut(2)
c = Nut(3)
a.next = b
b.next = c
c.next = b

print(co_chu_trinh(a))

d = Nut(1)
e = Nut(2)
d.next = e
print(co_chu_trinh(d))
