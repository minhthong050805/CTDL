import math
import heapq
def dijkstra_heap(ds_ke, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    hang_doi = [(0, nguon)]
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
nguon = 0
kc = dijkstra_heap(ds_ke, n, nguon)
print(f"dist = {kc}")
