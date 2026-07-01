class NutDoi:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bang_bam = {}
        self.head = NutDoi()
        self.tail = NutDoi()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _go_ra(self, nut):
        nut.prev.next = nut.next
        nut.next.prev = nut.prev

    def _them_vao_dau(self, nut):
        nut.next = self.head.next
        nut.prev = self.head
        self.head.next.prev = nut
        self.head.next = nut

    def get(self, key):
        if key not in self.bang_bam:
            return -1
        nut = self.bang_bam[key]
        self._go_ra(nut)
        self._them_vao_dau(nut)
        return nut.val

    def put(self, key, val):
        if key in self.bang_bam:
            nut = self.bang_bam[key]
            nut.val = val
            self._go_ra(nut)
            self._them_vao_dau(nut)
            return
        if len(self.bang_bam) == self.capacity:
            nut_cu = self.tail.prev
            self._go_ra(nut_cu)
            del self.bang_bam[nut_cu.key]
        nut_moi = NutDoi(key, val)
        self._them_vao_dau(nut_moi)
        self.bang_bam[key] = nut_moi


cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print(cache.get(1))
cache.put(3, 30)
print(cache.get(2))
print(cache.get(3))
