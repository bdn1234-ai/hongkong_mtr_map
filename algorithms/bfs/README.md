# BFS Algorithm API - Hướng dẫn sử dụng

## Mục tiêu
Module `bfs.py` cung cấp hàm tìm đường đi qua **ít ga nhất** (tối ưu số trạm dừng) giữa hai ga tàu sử dụng thuật toán **Breadth-First Search (BFS)**.

## Cách sử dụng

### Import module

```python
from bfs import bfs
from data_loader import GraphData
```

### Khởi tạo dữ liệu
```python
data = GraphData()
```

### Gọi thuật toán
```python
result = bfs(data, "Central", "Tung Chung")
```

### Kết quả trả về
```python
{
  "path": ["Central", "Hong Kong", "Kowloon", "Tsing Yi", "Tung Chung"],
  "total_stations": 5,
  "explored": ["Central", "Admiralty", "North Point"]
}
```

* `path`: Danh sách các ga từ điểm bắt đầu → điểm đích
* `total_station`: Tổng số ga trên lộ trình
* `explored`: Các node đã được duyệt (dùng để visualize/debug)

Nếu không tìm được: 
```python
None
```

### Đầu vào
```python
bfs(data, start, goal)
```

### Ví dụ đầy đủ
```python
from algorithms.bfs.bfs import bfs
from data.data_loader import GraphData

data = GraphData(
    graph_path="data/processed_data/graph.json",
    coords_path="data/processed_data/coords.json"
)

path = bfs(data, "Central", "Tung Chung")

if path:
    print("--- Tìm thấy đường đi ---")
    print("Lộ trình:", path)
    print("Số ga đi qua:", len(path))
else:
    print("Không tìm được đường đi")
```

### Tích hợp BE
FastAPI
```python
from fastapi import FastAPI
from algorithms.bfs.bfs import bfs
from data.data_loader import GraphData

app = FastAPI()
data = GraphData()

@app.get("/path")
def get_path(start: str, goal: str):
    path_list = bfs(data, start, goal)
    
    if not path_list:
        return {"error": "No path found"}
        
    return {
        "path": path_list, 
        "total_stations": len(path_list)
    }
```

### Tích hợp FE
```javascript
fetch("/path?start=Central&goal=Tung%20Chung")
  .then(res => res.json())
  .then(data => {
    if (data.error) {
        console.log("Lỗi:", data.error);
    } else {
        console.log("Lộ trình:", data.path);
        console.log("Số trạm dừng:", data.total_stations);
    }
  });
```

