import math
import heapq
import time
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
def xu_ly_tung_truy_van(ds_ke, n, danh_sach_truy_van):
    ket_qua = []
    for nguon, dich in danh_sach_truy_van:
        kc = dijkstra(ds_ke, n, nguon)
        ket_qua.append(kc[dich])
    return ket_qua
def xu_ly_tien_xu_ly(ds_ke, n, danh_sach_truy_van):
    tap_nguon = set(s for s, _ in danh_sach_truy_van)
    bang_kc = {}
    for nguon in tap_nguon:
        bang_kc[nguon] = dijkstra(ds_ke, n, nguon)
    ket_qua = []
    for nguon, dich in danh_sach_truy_van:
        ket_qua.append(bang_kc[nguon][dich])
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
danh_sach_truy_van = [(0, 4), (0, 5), (2, 3), (0, 3), (0, 5)]
t1 = time.time()
kq1 = xu_ly_tung_truy_van(ds_ke, n, danh_sach_truy_van)
t_tung = time.time() - t1
t1 = time.time()
kq2 = xu_ly_tien_xu_ly(ds_ke, n, danh_sach_truy_van)
t_tien = time.time() - t1
print(f"Ket qua: {kq1}")
print(f"Tung truy van: {t_tung:.6f}s")
print(f"Tien xu ly: {t_tien:.6f}s")
print("Chien luoc: Q lon + nhieu nguon trung lap -> tien xu ly; Q nho -> tung truy van")
