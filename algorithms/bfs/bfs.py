from collections import deque
from data_loader import GraphData

def bfs(data: GraphData, start: str, goal: str) -> list[str] | None:

    if not data.has_node(start) or not data.has_node(goal):
        return None
    
    if start == goal:
        return [start]

    queue = deque([start])

    camefrom = {start: None}

    while queue:
        current = queue.popleft() 

        if current == goal:
            return _reconstruct_path(camefrom, goal)


        for neighbor, _ in data.get_neighbors(current):
            if neighbor not in camefrom: 
                camefrom[neighbor] = current
                queue.append(neighbor)

    return None 

def _reconstruct_path(camefrom: dict, goal: str) -> list[str]:
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = camefrom[current]
    return list(reversed(path))