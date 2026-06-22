import math
import heapq
def dijkstra(ds_ke, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    cha = [-1] * n
    hang_doi = [(0, nguon)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                cha[v] = u
                heapq.heappush(hang_doi, (kc[v], v))
    return kc, cha
def truy_vet(cha, dich):
    duong_di = []
    u = dich
    while u != -1:
        duong_di.append(u)
        u = cha[u]
    return duong_di[::-1]
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
kc, cha = dijkstra(ds_ke, n, nguon)
duong_di = truy_vet(cha, dich)
print("Duong di:", " -> ".join(map(str, duong_di)))
print(f"Do dai: {kc[dich]}")
