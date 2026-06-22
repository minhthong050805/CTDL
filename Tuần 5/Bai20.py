import heapq
def k_duong_ngan_nhat(ds_ke, n, nguon, dich, k):
    so_lan_chot = [0] * n
    hang_doi = [(0, nguon)]
    ket_qua = []
    while hang_doi and len(ket_qua) < k:
        d, u = heapq.heappop(hang_doi)
        so_lan_chot[u] += 1
        if so_lan_chot[u] > k:
            continue
        if u == dich:
            ket_qua.append(d)
        for v, w in ds_ke[u]:
            if so_lan_chot[v] < k:
                heapq.heappush(hang_doi, (d + w, v))
    return ket_qua
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
k = 3
ket_qua = k_duong_ngan_nhat(ds_ke, n, nguon, dich, k)
print(f"{k} duong ngan nhat tu {nguon} den {dich}: {ket_qua}")
