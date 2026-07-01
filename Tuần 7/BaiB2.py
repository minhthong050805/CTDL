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


def do_dai(head):
    dem = 0
    nut = head
    while nut is not None:
        print(nut.val)
        dem += 1
        nut = nut.next
    return dem


head = tao_danh_sach([1, 2, 3])
print("Do dai:", do_dai(head))
