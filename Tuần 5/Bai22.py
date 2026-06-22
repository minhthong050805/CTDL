import math
import heapq
def dijkstra_gioi_han_canh(ds_ke, n, nguon, dich, k):
    kc = [[math.inf] * (k + 1) for _ in range(n)]
    kc[nguon][0] = 0
    hang_doi = [(0, nguon, 0)]
    while hang_doi:
        d, u, so_canh = heapq.heappop(hang_doi)
        if u == dich:
            return d
        if so_canh >= k:
            continue
        if d > kc[u][so_canh]:
            continue
        for v, w in ds_ke[u]:
            moi = d + w
            buoc_moi = so_canh + 1
            if moi < kc[v][buoc_moi]:
                kc[v][buoc_moi] = moi
                heapq.heappush(hang_doi, (moi, v, buoc_moi))
    ket_qua = min(kc[dich])
    return ket_qua if ket_qua != math.inf else -1
ds_ke = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}
n = 6
nguon = 0
dich = 4
k = 3
ket_qua = dijkstra_gioi_han_canh(ds_ke, n, nguon, dich, k)
print(f"Duong di ngan nhat tu {nguon} den {dich} voi toi da {k} canh: {ket_qua}")
