def tim_sinh_vien(ds, ma_sv):
    for i in range(len(ds)):
        if ds[i]["ma_sv"] == ma_sv:
            return ds[i]
    return None

ds_sinh_vien = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van A", "diem_tb": 8.5},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi B", "diem_tb": 7.2},
    {"ma_sv": "SV003", "ho_ten": "Le Van C", "diem_tb": 9.0},
]

ma_can_tim = "SV002"
ket_qua = tim_sinh_vien(ds_sinh_vien, ma_can_tim)

if ket_qua is not None:
    print("Ma SV:", ket_qua["ma_sv"])
    print("Ho ten:", ket_qua["ho_ten"])
    print("Diem TB:", ket_qua["diem_tb"])
else:
    print("Khong tim thay sinh vien co ma", ma_can_tim)
