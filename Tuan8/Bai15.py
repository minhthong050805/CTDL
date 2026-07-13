import hashlib
import bisect


class ConsistentHashRing:
    def __init__(self, virtual_nodes=100):
        self.virtual_nodes = virtual_nodes
        self.ring = {}
        self.sorted_hashes = []
        self.servers = set()

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_server(self, server):
        self.servers.add(server)
        for i in range(self.virtual_nodes):
            vnode_key = f"{server}#{i}"
            h = self._hash(vnode_key)
            self.ring[h] = server
            bisect.insort(self.sorted_hashes, h)

    def remove_server(self, server):
        self.servers.discard(server)
        for i in range(self.virtual_nodes):
            vnode_key = f"{server}#{i}"
            h = self._hash(vnode_key)
            if h in self.ring:
                del self.ring[h]
                idx = bisect.bisect_left(self.sorted_hashes, h)
                self.sorted_hashes.pop(idx)

    def get_server(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self.sorted_hashes, h)
        if idx == len(self.sorted_hashes):
            idx = 0
        return self.ring[self.sorted_hashes[idx]]


ring = ConsistentHashRing(virtual_nodes=100)
for s in ["server-1", "server-2", "server-3"]:
    ring.add_server(s)

keys = [f"key-{i}" for i in range(1000)]
mapping_before = {k: ring.get_server(k) for k in keys}

ring.add_server("server-4")
mapping_after = {k: ring.get_server(k) for k in keys}

moved = sum(1 for k in keys if mapping_before[k] != mapping_after[k])

print("Da them 3 server ban dau: server-1, server-2, server-3")
print(f"Phan bo 1000 khoa truoc khi them server-4:")
for s in sorted(set(mapping_before.values())):
    cnt = sum(1 for v in mapping_before.values() if v == s)
    print(f"  {s}: {cnt} khoa")

print()
print("Them server-4 vao vong bam...")
print(f"So khoa phai di chuyen sang server khac: {moved} / {len(keys)} "
      f"(~{moved / len(keys) * 100:.1f}%)")
print(f"Ky vong ly thuyet neu chia deu cho 4 server: ~{100 / 4:.1f}%")

print()
print(f"Phan bo 1000 khoa sau khi them server-4:")
for s in sorted(set(mapping_after.values())):
    cnt = sum(1 for v in mapping_after.values() if v == s)
    print(f"  {s}: {cnt} khoa")
