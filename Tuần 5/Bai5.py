import math
ds_ke = {
    'A': [('B', 5), ('C', 3), ('D', 1)],
    'B': [('A', 5), ('D', 2)],
    'C': [('A', 3), ('D', 6)],
    'D': [('A', 1), ('B', 2), ('C', 6), ('E', 4)],
    'E': [('D', 4)]
}
def dijkstra(ds_ke, nguon):
    dinh_sach = list(ds_ke.keys())
    kc = {d: math.inf for d in dinh_sach}
    kc[nguon] = 0
    da_chot = set()
    for _ in range(len(dinh_sach)):
        u = min((v for v in dinh_sach if v not in da_chot), key=lambda v: kc[v])
        da_chot.add(u)
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc
nguon = 'A'
kc = dijkstra(ds_ke, nguon)
for dinh, d in kc.items():
    print(f"dist[{dinh}] = {d if d != math.inf else -1}")
