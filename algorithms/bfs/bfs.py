from collections import deque
from data.data_loader import GraphData

def bfs(data: GraphData, start: str, goal: str) -> dict | None:

    if not data.has_node(start) or not data.has_node(goal):
        return None
    
    if start == goal:
        return [start]

    queue = deque([start])

    camefrom = {start: None}
    explored = []

    while queue:
        current = queue.popleft() 
        explored.append(current)

        if current == goal:
            
            path = [current]
            while current != start:
                current = camefrom[current]
                path.append(current)
            path = list(reversed(path))
            
            return {
                "path": path,
                "cost": len(path) - 1,   
                "explored": explored
            }


        for neighbor, _ in data.get_neighbors(current):
            if neighbor not in camefrom: 
                camefrom[neighbor] = current
                queue.append(neighbor)

    return None 

# data = GraphData()
# result = bfs(data, "Central", "Hung Hom")
# print(result)
