danh_ba = []

def them_lien_he(ten, sdt):
    danh_ba.append({"ten": ten, "sdt": sdt})

def tim_sdt_theo_ten(ten):
    for i in range(len(danh_ba)):
        if danh_ba[i]["ten"].lower() == ten.lower():
            return danh_ba[i]["sdt"]
    return None

def tim_ten_theo_sdt(sdt):
    for i in range(len(danh_ba)):
        if danh_ba[i]["sdt"] == sdt:
            return danh_ba[i]["ten"]
    return None

def dem_theo_dau_so(dau_so):
    dem = 0
    for i in range(len(danh_ba)):
        if danh_ba[i]["sdt"].startswith(dau_so):
            dem += 1
    return dem

def menu():
    while True:
        print("1. Them lien he")
        print("2. Tim so dien thoai theo ten")
        print("3. Tim ten theo so dien thoai")
        print("4. Dem so lien he theo dau so")
        print("5. Thoat")
        chon = input("Chon chuc nang: ")

        if chon == "1":
            ten = input("Nhap ten: ")
            sdt = input("Nhap so dien thoai: ")
            them_lien_he(ten, sdt)
        elif chon == "2":
            ten = input("Nhap ten can tim: ")
            ket_qua = tim_sdt_theo_ten(ten)
            if ket_qua is not None:
                print("So dien thoai:", ket_qua)
            else:
                print("Khong tim thay")
        elif chon == "3":
            sdt = input("Nhap so dien thoai can tim: ")
            ket_qua = tim_ten_theo_sdt(sdt)
            if ket_qua is not None:
                print("Ten:", ket_qua)
            else:
                print("Khong tim thay")
        elif chon == "4":
            dau_so = input("Nhap dau so can dem: ")
            print("So luong:", dem_theo_dau_so(dau_so))
        elif chon == "5":
            break
        else:
            print("Lua chon khong hop le")

menu()
