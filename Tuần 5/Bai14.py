import math
import heapq
def duong_ngan_nhi(ds_ke, n, nguon, dich):
    kc = [[math.inf, math.inf] for _ in range(n)]
    kc[nguon][0] = 0
    hang_doi = [(0, nguon)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > kc[u][1]:
            continue
        for v, w in ds_ke[u]:
            moi = d + w
            if moi < kc[v][0]:
                kc[v][1] = kc[v][0]
                kc[v][0] = moi
                heapq.heappush(hang_doi, (moi, v))
            elif kc[v][0] < moi < kc[v][1]:
                kc[v][1] = moi
                heapq.heappush(hang_doi, (moi, v))
    return kc[dich][0], kc[dich][1]
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
ngan_nhat, ngan_nhi = duong_ngan_nhi(ds_ke, n, nguon, dich)
print(f"Ngan nhat: {ngan_nhat}")
print(f"Ngan nhi: {ngan_nhi if ngan_nhi != math.inf else -1}")
