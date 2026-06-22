import math
def dijkstra(ds_ke, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    da_chot = [False] * n
    for _ in range(n):
        u = min((v for v in range(n) if not da_chot[v]), key=lambda v: kc[v])
        da_chot[u] = True
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
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
kc = dijkstra(ds_ke, n, nguon)
print(f"dist = {kc}")
