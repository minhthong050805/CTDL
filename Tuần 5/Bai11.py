import math
import heapq
def dijkstra_nhieu_nguon(ds_ke, n, tap_nguon):
    kc = [math.inf] * n
    hang_doi = []
    for nguon in tap_nguon:
        kc[nguon] = 0
        heapq.heappush(hang_doi, (0, nguon))
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                heapq.heappush(hang_doi, (kc[v], v))
    return kc
ds_ke = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}
n = 6
tap_nguon = {0, 3}
kc = dijkstra_nhieu_nguon(ds_ke, n, tap_nguon)
print(f"Tap nguon: {tap_nguon}")
for i in range(n):
    print(f"dist[{i}] = {kc[i] if kc[i] != math.inf else -1}")
