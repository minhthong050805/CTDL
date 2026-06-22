import math
import heapq
def dijkstra(ds_ke, n, nguon, dich):
    kc = [math.inf] * n
    kc[nguon] = 0
    hang_doi = [(0, nguon)]
    so_dinh_duyet = 0
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        so_dinh_duyet += 1
        if u == dich:
            return kc[dich], so_dinh_duyet
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                heapq.heappush(hang_doi, (kc[v], v))
    return kc[dich], so_dinh_duyet
def bellman_ford(ds_canh, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    for _ in range(n - 1):
        for u, v, w in ds_canh:
            if kc[u] != math.inf and kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    for u, v, w in ds_canh:
        if kc[u] != math.inf and kc[u] + w < kc[v]:
            return None
    return kc
def astar(ds_ke, n, nguon, dich, heuristic):
    kc = [math.inf] * n
    kc[nguon] = 0
    hang_doi = [(heuristic(nguon), 0, nguon)]
    so_dinh_duyet = 0
    while hang_doi:
        f, g, u = heapq.heappop(hang_doi)
        so_dinh_duyet += 1
        if u == dich:
            return kc[dich], so_dinh_duyet
        if g > kc[u]:
            continue
        for v, w in ds_ke[u]:
            g_moi = kc[u] + w
            if g_moi < kc[v]:
                kc[v] = g_moi
                f_moi = g_moi + heuristic(v)
                heapq.heappush(hang_doi, (f_moi, g_moi, v))
    return kc[dich], so_dinh_duyet
ds_ke = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}
ds_canh = [(0, 1, 4), (0, 2, 1), (1, 3, 1), (2, 1, 2), (2, 3, 5), (2, 4, 8), (3, 4, 3), (3, 5, 6), (4, 5, 2)]
n = 6
nguon = 0
dich = 4
vi_tri = {0: 0, 1: 2, 2: 1, 3: 1.5, 4: 3, 5: 4}
def heuristic(v):
    return abs(vi_tri[v] - vi_tri[dich])
d_dijk, duyet_dijk = dijkstra(ds_ke, n, nguon, dich)
kc_bf = bellman_ford(ds_canh, n, nguon)
d_astar, duyet_astar = astar(ds_ke, n, nguon, dich, heuristic)
print(f"Dijkstra: dist={d_dijk}, so dinh duyet={duyet_dijk}, O((V+E)logV), chi hoat dong voi trong so >= 0")
print(f"Bellman-Ford: dist={kc_bf[dich]}, O(VE), hoat dong voi canh am, phat hien chu trinh am")
print(f"A*: dist={d_astar}, so dinh duyet={duyet_astar}, O((V+E)logV), heuristic giup duyet it dinh hon")
