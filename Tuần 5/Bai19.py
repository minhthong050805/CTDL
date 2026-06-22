import heapq
def xac_suat_lon_nhat(ds_ke, n, nguon, dich):
    xac_suat = [0.0] * n
    xac_suat[nguon] = 1.0
    hang_doi = [(-1.0, nguon)]
    while hang_doi:
        p, u = heapq.heappop(hang_doi)
        p = -p
        if u == dich:
            return xac_suat[dich]
        if p < xac_suat[u]:
            continue
        for v, xs in ds_ke[u]:
            moi = xac_suat[u] * xs
            if moi > xac_suat[v]:
                xac_suat[v] = moi
                heapq.heappush(hang_doi, (-moi, v))
    return xac_suat[dich]
ds_ke = {
    0: [(1, 0.5), (2, 0.8)],
    1: [(3, 0.9)],
    2: [(1, 0.7), (3, 0.6)],
    3: []
}
n = 4
nguon = 0
dich = 3
ket_qua = xac_suat_lon_nhat(ds_ke, n, nguon, dich)
print(f"Xac suat lon nhat tu {nguon} den {dich} = {ket_qua:.4f}")
