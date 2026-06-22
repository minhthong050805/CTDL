import math
ds_ke = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5), (4, 8)],
    3: [(4, 3), (5, 6)],
    4: [(5, 2)],
    5: []
}
n = 6
kc = [math.inf] * n
kc[0] = 0
da_chot = [False] * n
thu_tu_chot = []
print(f"{'Vong':>5} | {'Dinh chot':>10} | {' '.join(f'd[{i}]' for i in range(n))}")
for _ in range(n):
    u = min((v for v in range(n) if not da_chot[v]), key=lambda v: kc[v])
    da_chot[u] = True
    thu_tu_chot.append(u)
    for v, w in ds_ke[u]:
        if kc[u] + w < kc[v]:
            kc[v] = kc[u] + w
    dong_kc = ' '.join(f'{kc[i] if kc[i] != math.inf else "inf":>4}' for i in range(n))
    print(f"{len(thu_tu_chot):>5} | {u:>10} | {dong_kc}")
print("Thu tu chot:", thu_tu_chot)
