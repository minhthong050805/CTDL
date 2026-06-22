import math
def dijkstra_v2(ds_ke, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    da_chot = [False] * n
    for _ in range(n):
        u = min((v for v in range(n) if not da_chot[v]), key=lambda v: kc[v])
        da_chot[u] = True
        for v, w in ds_ke[u]:
            if not da_chot[v] and kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc
def bellman_ford(ds_canh, n, nguon):
    kc = [math.inf] * n
    kc[nguon] = 0
    for _ in range(n - 1):
        for u, v, w in ds_canh:
            if kc[u] != math.inf and kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
    return kc
ds_ke = {
    0: [(1, 2), (2, 5)],
    1: [],
    2: [(1, -4)]
}
ds_canh = [(0, 1, 2), (0, 2, 5), (2, 1, -4)]
n = 3
nguon = 0
kc_dijkstra = dijkstra_v2(ds_ke, n, nguon)
kc_bellman = bellman_ford(ds_canh, n, nguon)
print(f"Dijkstra O(V^2): dist[1] = {kc_dijkstra[1]} (SAI, dung phai la 1)")
print(f"Bellman-Ford:    dist[1] = {kc_bellman[1]} (DUNG)")
print()
print("Giai thich:")
print("  Vong 1: chot dinh 0. Relax: dist[1]=2, dist[2]=5.")
print("  Vong 2: chot dinh 1 (dist[1]=2 < dist[2]=5). Dinh 1 da chot.")
print("  Vong 3: chot dinh 2. Xu ly canh 2->1 (-4), nhung dinh 1 da chot -> bo qua.")
print("  Ket qua: dist[1]=2 thay vi 1 (duong 0->2->1 = 5-4 = 1).")
print("  => Dijkstra sai khi co canh am. Dung Bellman-Ford thay the.")
