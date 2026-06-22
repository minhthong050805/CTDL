import math
import heapq
def dijkstra(ds_ke, n, nguon, dich):
    kc = [math.inf] * n
    kc[nguon] = 0
    hang_doi = [(0, nguon)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if u == dich:
            return kc[dich]
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                heapq.heappush(hang_doi, (kc[v], v))
    return kc[dich] if kc[dich] != math.inf else -1
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
ket_qua = dijkstra(ds_ke, n, nguon, dich)
print(f"dist({nguon} -> {dich}) = {ket_qua}")
