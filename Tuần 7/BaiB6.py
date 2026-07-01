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


def dao_nguoc_lap(head):
    truoc = None
    hien_tai = head
    while hien_tai is not None:
        tiep = hien_tai.next
        hien_tai.next = truoc
        truoc = hien_tai
        hien_tai = tiep
    return truoc


def dao_nguoc_de_quy(head):
    if head is None or head.next is None:
        return head
    head_moi = dao_nguoc_de_quy(head.next)
    head.next.next = head
    head.next = None
    return head_moi


def in_toan_bo(head):
    nut = head
    ket_qua = []
    while nut is not None:
        ket_qua.append(str(nut.val))
        nut = nut.next
    print("->".join(ket_qua) + "->null")


head1 = tao_danh_sach([1, 2, 3])
in_toan_bo(dao_nguoc_lap(head1))

head2 = tao_danh_sach([1, 2, 3])
in_toan_bo(dao_nguoc_de_quy(head2))
