import heapq
from data.data_loader import GraphData


def greedy(data: GraphData, src: str, des: str) -> dict | None:
    # Validate
    if not data.has_node(src):
        print(f"[Greedy] Unknown station: '{src}'")
        return None
    if not data.has_node(des):
        print(f"[Greedy] Unknown station: '{des}'")
        return None
    if src == des:
        return {"path": [src], "cost": 0.0, "explored": []}

    # Data structures
    fringe = [(data.heuristic(src, des), src)]  
    parent = {}
    visited = set()
    explored = []

    while fringe:
        h, current = heapq.heappop(fringe)

        if current in visited:
            continue

        visited.add(current)
        explored.append(current)

        # Found goal
        if current == des:
            # Retrace path
            path = [current]
            while current != src:
                current = parent[current]
                path.append(current)
            path = list(reversed(path))
            
            # Compute cost
            cost = 0.0
            for i in range(len(path) - 1):
                cost += data.get_cost(path[i], path[i+1])
                
            return {
                "path": path,
                "cost": round(cost, 4),
                "explored": explored
            }

        # Expand neighbors
        for neighbor, _ in data.get_neighbors(current):
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(fringe, (data.heuristic(neighbor, des), neighbor))

    return None


# data = GraphData()
# result = greedy(data, "Central", "Hung Hom")
# print(result, data.heuristic("Central", "Hung Hom"))
