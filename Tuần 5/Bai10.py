import math
import heapq
import time
import random
def dijkstra_v2(ds_ke, n, nguon):
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
def tao_do_thi(n, mat_do):
    ds_ke = {i: [] for i in range(n)}
    so_canh = int(n * (n - 1) * mat_do)
    them = set()
    while len(them) < so_canh:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and (u, v) not in them:
            them.add((u, v))
            ds_ke[u].append((v, random.randint(1, 10)))
    return ds_ke
n = 100
for mat_do, ten in [(0.05, "Thua (E~V)"), (0.9, "Day (E~V^2)")]:
    ds_ke = tao_do_thi(n, mat_do)
    t1 = time.time()
    dijkstra_v2(ds_ke, n, 0)
    t_v2 = time.time() - t1
    t1 = time.time()
    dijkstra_heap(ds_ke, n, 0)
    t_heap = time.time() - t1
    print(f"{ten}: O(V^2)={t_v2:.4f}s, Heap={t_heap:.4f}s")
print("\nPhan tich:")
print("E ~ V^2 (do thi day): O(V^2) tuong duong heap, it overhead hon")
print("E ~ V   (do thi thua): Heap O((V+E)logV) << O(V^2)")
