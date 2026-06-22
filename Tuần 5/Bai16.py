import math
import heapq
def dijkstra_trong_so_dinh(ds_ke_goc, chi_phi_dinh, n, nguon, dich):
    ds_ke = {i: [] for i in range(2 * n)}
    for u in range(n):
        ds_ke[2 * u].append((2 * u + 1, chi_phi_dinh[u]))
    for u, hang_xom in ds_ke_goc.items():
        for v, _ in hang_xom:
            ds_ke[2 * u + 1].append((2 * v, 0))
    kc = [math.inf] * (2 * n)
    kc[2 * nguon] = chi_phi_dinh[nguon]
    hang_doi = [(chi_phi_dinh[nguon], 2 * nguon)]
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        if d > kc[u]:
            continue
        for v, w in ds_ke[u]:
            if kc[u] + w < kc[v]:
                kc[v] = kc[u] + w
                heapq.heappush(hang_doi, (kc[v], v))
    return kc[2 * dich + 1]
ds_ke_goc = {
    0: [(1, 0), (2, 0)],
    1: [(3, 0)],
    2: [(1, 0), (3, 0), (4, 0)],
    3: [(4, 0), (5, 0)],
    4: [(5, 0)],
    5: []
}
chi_phi_dinh = [0, 4, 1, 2, 3, 6]
n = 6
nguon = 0
dich = 4
ket_qua = dijkstra_trong_so_dinh(ds_ke_goc, chi_phi_dinh, n, nguon, dich)
print(f"Chi phi ngan nhat qua dinh tu {nguon} den {dich} = {ket_qua}")
