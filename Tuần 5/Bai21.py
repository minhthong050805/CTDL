import math
import heapq
def dijkstra_trang_thai(ds_ke, n, nguon, dich, nhien_lieu_toi_da):
    kc = [[math.inf] * (nhien_lieu_toi_da + 1) for _ in range(n)]
    kc[nguon][nhien_lieu_toi_da] = 0
    hang_doi = [(0, nguon, nhien_lieu_toi_da)]
    while hang_doi:
        chi_phi, u, nhien_lieu = heapq.heappop(hang_doi)
        if chi_phi > kc[u][nhien_lieu]:
            continue
        for v, w in ds_ke[u]:
            if nhien_lieu >= w:
                nhien_lieu_con = nhien_lieu - w
                moi_chi_phi = chi_phi + 1
                if moi_chi_phi < kc[v][nhien_lieu_con]:
                    kc[v][nhien_lieu_con] = moi_chi_phi
                    heapq.heappush(hang_doi, (moi_chi_phi, v, nhien_lieu_con))
    ket_qua = min(kc[dich])
    return ket_qua if ket_qua != math.inf else -1
ds_ke = {
    0: [(1, 3), (2, 1)],
    1: [(3, 2)],
    2: [(3, 4)],
    3: []
}
n = 4
nguon = 0
dich = 3
nhien_lieu_toi_da = 5
ket_qua = dijkstra_trang_thai(ds_ke, n, nguon, dich, nhien_lieu_toi_da)
print(f"Chi phi ngan nhat tu {nguon} den {dich} voi nhien lieu toi da {nhien_lieu_toi_da}: {ket_qua}")
