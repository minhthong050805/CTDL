import math
import heapq
def dem_duong_ngan_nhat(ds_ke, n, nguon):
    kc = [math.inf] * n
    so_duong = [0] * n
    kc[nguon] = 0
    so_duong[nguon] = 1
    hang_doi = [(0, nguon)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            moi = kc[u] + w
            if moi < kc[v]:
                kc[v] = moi
                so_duong[v] = so_duong[u]
                heapq.heappush(hang_doi, (kc[v], v))
            elif moi == kc[v]:
                so_duong[v] += so_duong[u]
    return kc, so_duong
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
kc, so_duong = dem_duong_ngan_nhat(ds_ke, n, nguon)
for i in range(n):
    print(f"dist[{i}] = {kc[i] if kc[i] != math.inf else 'inf'}, so duong = {so_duong[i]}")
