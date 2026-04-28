# A* Algorithm API - Hướng dẫn sử dụng

## Mục tiêu

Module `astar.py` cung cấp hàm tìm đường đi ngắn nhất giữa hai node (ga tàu) sử dụng thuật toán **A***.

Module này được thiết kế để:

* Hoạt động độc lập với UI (frontend)
* Dễ dàng tích hợp vào backend (API)
* Tận dụng `GraphData` từ `data_loader.py`



## Cách sử dụng

### Import module

```python
from astar import astar
from data_loader import GraphData
```



### Khởi tạo dữ liệu

```python
data = GraphData()
```



### Gọi thuật toán

```python
result = astar(data, "Central", "Tung Chung")
```



## Kết quả trả về

Nếu tìm được đường đi:

```python
{
  "path": ["Central", "Hong Kong", "Kowloon", "Tsing Yi"],
  "cost": 15.2345,
  "explored": ["Central", "Admiralty", "Hong Kong"]
}
```

### Ý nghĩa:

* `path`: Danh sách các ga từ điểm bắt đầu → điểm đích
* `cost`: Tổng chi phí (khoảng cách)
* `explored`: Các node đã được duyệt (dùng để visualize/debug)



Nếu không tìm được đường:

```python
None
```



## Yêu cầu đầu vào

```python
astar(data, start, goal)
```

* `data`: instance của `GraphData`
* `start`: tên ga bắt đầu (string)
* `goal`: tên ga đích (string)



## Ví dụ đầy đủ

```python
from astar import astar
from data_loader import GraphData

data = GraphData()

result = astar(data, "Central", "Tung Chung")

if result:
    print("Path:", result["path"])
    print("Cost:", result["cost"])
else:
    print("Không tìm được đường đi")
```



## Cách hoạt động (tóm tắt)

Thuật toán A* sử dụng:

* `g(n)`: chi phí thực từ start → n
* `h(n)`: heuristic (ước lượng từ n → goal)
* `f(n) = g(n) + h(n)`

Node có `f(n)` nhỏ nhất sẽ được ưu tiên duyệt trước.



## Tích hợp Backend

Ví dụ với FastAPI:

```python
from fastapi import FastAPI
from astar import astar
from data_loader import GraphData

app = FastAPI()
data = GraphData()

@app.get("/path")
def get_path(start: str, goal: str):
    result = astar(data, start, goal)

    if result is None:
        return {"error": "Không tìm được đường"}

    return result
```



## Tích hợp Frontend

Frontend chỉ cần gọi API:

```javascript
fetch("/path?start=Central&goal=Tung%20Chung")
  .then(res => res.json())
  .then(data => {
    console.log(data.path);
    console.log(data.cost);
  });
```