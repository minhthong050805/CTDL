import math
import heapq
def dijkstra(ds_ke, n, nguon):
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
def dijkstra_qua_diem(ds_ke, n, nguon, dich, bat_buoc):
    kc_tu_nguon = dijkstra(ds_ke, n, nguon)
    kc_tu_bat_buoc = dijkstra(ds_ke, n, bat_buoc)
    d1 = kc_tu_nguon[bat_buoc]
    d2 = kc_tu_bat_buoc[dich]
    if d1 == math.inf or d2 == math.inf:
        return -1
    return d1 + d2
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
dich = 5
bat_buoc = 2
ket_qua = dijkstra_qua_diem(ds_ke, n, nguon, dich, bat_buoc)
print(f"Duong di {nguon} -> {bat_buoc} -> {dich} = {ket_qua}")
