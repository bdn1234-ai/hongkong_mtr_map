# Data Loader API - Hướng dẫn sử dụng

## Mục tiêu

Module `data_loader.py` cung cấp các hàm API giúp truy cập dữ liệu đồ thị (graph) và tọa độ (coordinates) một cách dễ dàng, phục vụ cho các thuật toán như **A*** và **Dijkstra**.



## Cấu trúc dữ liệu

### 1. `graph.json`

Lưu dưới dạng danh sách kề (adjacency list):

```json
{
  "Central": [["Admiralty", 1.2]],
  "Admiralty": [["Central", 1.2], ["Wan Chai", 1.0]]
}
```



### 2. `coords.json`

Lưu tọa độ của các ga:

```json
{
  "Central": [22.2819, 114.1589],
  "Admiralty": [22.2795, 114.1650]
}
```



## Cách sử dụng

### Import module

```python
from data_loader import GraphData
```



### Khởi tạo

```python
data = GraphData()
```



## API chính

### 1. Lấy các node kề

```python
neighbors = data.get_neighbors("Central")
```

Kết quả:

```python
[["Admiralty", 1.2]]
```



### 2. Lấy cost giữa 2 node

```python
cost = data.get_cost("Central", "Admiralty")
```

Kết quả:

```python
1.2
```



### 3. Lấy tọa độ

```python
coord = data.get_coord("Central")
```

Kết quả:

```python
[22.2819, 114.1589]
```



### 4. Heuristic (dùng cho A*)

```python
h = data.heuristic("Central", "Mong Kok")
```

Trả về khoảng cách ước lượng giữa 2 node



### 5. Lấy toàn bộ node

```python
nodes = data.get_nodes()
```



### 6. Kiểm tra node tồn tại

```python
exists = data.has_node("Central")
```



## Ví dụ dùng trong A*

```python
for neighbor, cost in data.get_neighbors(current):
    new_cost = g_score[current] + cost
```

