def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
      return -1
array=[20,30,15,5,10,40]
x=40
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)
def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
    return -1
array=[15,25,80,30,60,50,110,100,130,180]
x=110;
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)


def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
    return -1
array=[15,25,80,30,60,50,110,100,130,180]
x=185;
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)

danh_ba = []

while True:
    print("\n===== MENU =====")
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số điện thoại bắt đầu bằng đầu số cho trước")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn: "))
    if chon == 1:
        ten = input("Nhập tên: ")
        sdt = input("Nhập số điện thoại: ")

        lien_he = {
            "ten": ten,
            "sdt": sdt
        }

        danh_ba.append(lien_he)
        print("Đã thêm liên hệ")
    elif chon == 2:
        ten_can_tim = input("Nhập tên cần tìm: ")

        tim_thay = False

        for lh in danh_ba:
            if lh["ten"] == ten_can_tim:
                print("Số điện thoại:", lh["sdt"])
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy")
    elif chon == 3:
        sdt_can_tim = input("Nhập số điện thoại cần tìm: ")

        tim_thay = False

        for lh in danh_ba:
            if lh["sdt"] == sdt_can_tim:
                print("Tên:", lh["ten"])
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy")
    elif chon == 4:
        dau_so = input("Nhập đầu số: ")

        dem = 0

        for lh in danh_ba:
            if lh["sdt"].startswith(dau_so):
                dem += 1

        print("Số lượng:", dem)
    elif chon == 0:
        print("Kết thúc chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        return -1
arr =['Bao','An','Dat','Duc','Hung','Phi','Vinh','Dung']
key = 'Phi'
print("vi tri tim thay thu i la"+str(linearsearch(arr,key)))def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(value)

x = int(input("nhap gia tri can tim "))

kq = linearsearch(a, x)

if kq != -1:
    print("tim thay tai vi tri",kq)
else:
    print("khong tim thay ")def tontai(a, x):
    for i in a:
        if i == x:
            return True
    return False

a = [1, 2, 3, 4, 5]
x = 3

print(tontai(a, x))def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
      return -1
array=[20,30,15,5,10,40]
x=40
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)
def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
    return -1
array=[15,25,80,30,60,50,110,100,130,180]
x=110;
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)


def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
    return -1
array=[15,25,80,30,60,50,110,100,130,180]
x=185;
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)

danh_ba = []

while True:
    print("\n===== MENU =====")
    print("1. Thêm liên hệ")
    print("2. Tìm số điện thoại theo tên")
    print("3. Tìm tên theo số điện thoại")
    print("4. Đếm số điện thoại bắt đầu bằng đầu số cho trước")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn: "))
    if chon == 1:
        ten = input("Nhập tên: ")
        sdt = input("Nhập số điện thoại: ")

        lien_he = {
            "ten": ten,
            "sdt": sdt
        }

        danh_ba.append(lien_he)
        print("Đã thêm liên hệ")
    elif chon == 2:
        ten_can_tim = input("Nhập tên cần tìm: ")

        tim_thay = False

        for lh in danh_ba:
            if lh["ten"] == ten_can_tim:
                print("Số điện thoại:", lh["sdt"])
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy")
    elif chon == 3:
        sdt_can_tim = input("Nhập số điện thoại cần tìm: ")

        tim_thay = False

        for lh in danh_ba:
            if lh["sdt"] == sdt_can_tim:
                print("Tên:", lh["ten"])
                tim_thay = True

        if not tim_thay:
            print("Không tìm thấy")
    elif chon == 4:
        dau_so = input("Nhập đầu số: ")

        dem = 0

        for lh in danh_ba:
            if lh["sdt"].startswith(dau_so):
                dem += 1

        print("Số lượng:", dem)
    elif chon == 0:
        print("Kết thúc chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")def linearsearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
        return -1
arr =['Bao','An','Dat','Duc','Hung','Phi','Vinh','Dung']
key = 'Phi'
print("vi tri tim thay thu i la"+str(linearsearch(arr,key)))def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


n = int(input("Nhập số phần tử: "))

a = []

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(value)

x = int(input("nhap gia tri can tim "))

kq = linearsearch(a, x)

if kq != -1:
    print("tim thay tai vi tri",kq)
else:
    print("khong tim thay ")def tontai(a, x):
    for i in a:
        if i == x:
            return True
    return False

a = [1, 2, 3, 4, 5]
x = 3

print(tontai(a, x))def tuyentinh(array, n, x):
    for i in range(0, n):
      if (array[i] == x):
        return i
      return -1
array=[20,30,15,5,10,40]
x=40
n=len(array)
result= tuyentinh(array,n,x)
print("phan tu tim thay duoc tai vi tri la",result)
def tuyentinh(array, n, x):
   