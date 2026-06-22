import math
import heapq
def dijkstra_luoi(luoi):
    hang = len(luoi)
    cot = len(luoi[0])
    kc = [[math.inf] * cot for _ in range(hang)]
    kc[0][0] = luoi[0][0]
    hang_doi = [(luoi[0][0], 0, 0)]
    huong = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while hang_doi:
        d, r, c = heapq.heappop(hang_doi)
        if d > kc[r][c]:
            continue
        for dr, dc in huong:
            nr, nc = r + dr, c + dc
            if 0 <= nr < hang and 0 <= nc < cot:
                moi = kc[r][c] + luoi[nr][nc]
                if moi < kc[nr][nc]:
                    kc[nr][nc] = moi
                    heapq.heappush(hang_doi, (moi, nr, nc))
    return kc[hang - 1][cot - 1]
luoi = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
ket_qua = dijkstra_luoi(luoi)
print(f"Chi phi nho nhat tu (0,0) den ({len(luoi)-1},{len(luoi[0])-1}) = {ket_qua}")
