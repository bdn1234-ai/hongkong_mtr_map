from data.data_loader import GraphData

data = GraphData()

# Admin thực hiện cấm đường
data.unblock_station_path("Central", "Admiralty") 
# Lệnh này vừa lưu vào file, vừa cập nhật logic cho get_neighbors ngay lập tức

# Khi chạy thuật toán (A*, BFS...), nó tự động bỏ qua đoạn đường này
# vì hàm get_neighbors đã được lọc qua self.traffic.is_blocked