Bai 1 : Nếu tìm thấy phần tử bằng với giá trị cần tìm thì trả về vị trí của phần tử đó. Nếu duyệt hết mảng mà vẫn không tìm thấy thì trả về -1. Input Mảng A gồm n phần tử. Giá trị cần tìm x. Output Vị trí của x trong mảng nếu tìm thấy. Trả về −1 nếu không tìm thấy. Thuật toán dừng khi Tìm thấy phần tử A\[i]=x. Hoặc đã kiểm tra hết tất cả phần tử trong mảng.



Bai 2 : B1 i =0 B2 a\[0]= 7 != 5 =x B3 i = 0+1=1



B.2: a\[1] = 3 != 5 = x



B.3: i = 1 + 1 = 2



B.2: a\[2] = 9 != 5 = x



B.3: i = 2 + 1 = 3



B.2: a\[3] = 12 != 5 = x



B.3: i = 3 + 1 = 4



B.2: a\[4] = 5 = x Tìm thấy khóa x tại vị trí i = 4. Dừng kết thúc



Bai 3 : A=\[3, 5, 7, 9, 11] Tìm x=7 So sánh lần lượt:



3 khác 7 5 khác 7 7 bằng 7



Tìm thấy x tại vị trí thứ 3



Số phép so sánh là:



3 phép so sánh.



x = 1



So sánh lần lượt:



3 khác 1 5 khác 1 7 khác 1 9 khác 1 11 khác 1



Không tìm thấy x trong mảng



Số phép so sánh là:



5 phép so sánh.



x = 100



So sánh lần lượt:



3 khác 100 5 khác 100 7 khác 100 9 khác 100 11 khác 100



Không tìm thấy x trong mảng Số phép so sánh là



5 phép so sánh Trường hợp tốt nhất



Phần tử cần tìm nằm ở đầu mảng.



Chỉ cần 1 phép so sánh.



Độ phức tạp:



O(1)



Trường hợp xấu nhất



Phần tử nằm cuối mảng hoặc không tồn tại trong mảng.



Phải duyệt hết n phần tử.



Số phép so sánh:



n phép so sánh.



Độ phức tạp:



O(n)



Trường hợp trung bình



Số phép so sánh trung bình:



(1 + 2 + 3 + ... + n) / n



n 1+2+3+⋯+n​



= 2 n+1​



Suy ra:



T(n) ≈ n/2



Độ phức tạp:



O(n)



BÀI 5. ĐIỀU KIỆN ÁP DỤNG



Tìm kiếm tuyến tính không yêu cầu mảng phải được sắp xếp.



Thuật toán sẽ kiểm tra lần lượt từng phần tử trong mảng cho đến khi tìm thấy phần tử cần tìm hoặc duyệt hết mảng.



Do đó có thể áp dụng cho:



Mảng đã sắp xếp Mảng chưa sắp xếp So sánh với tìm kiếm nhị phân Tìm kiếm tuyến tính Tìm kiếm nhị phân Không cần sắp xếp Phải sắp xếp trước Duyệt từng phần tử Chia đôi mảng Độ phức tạp O(n) Độ phức tạp O(log n) Dễ thực hiện Phức tạp hơn Kết luận Tìm kiếm tuyến tính đơn giản, dễ cài đặt. Phù hợp với dữ liệu nhỏ hoặc chưa sắp xếp. Tìm kiếm nhị phân nhanh hơn nhưng yêu cầu dữ liệu phải được sắp xếp trước

