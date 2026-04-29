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
            path = _reconstruct(parent, src, des)
            cost = _compute_cost(data, path)
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


def _reconstruct(parent: dict, src: str, goal: str) -> list[str]:
    path = [goal]
    current = goal

    while current != src:
        current = parent[current]
        path.append(current)

    return list(reversed(path))


def _compute_cost(data: GraphData, path: list[str]) -> float:
    cost = 0.0
    for i in range(len(path) - 1):
        for neighbor, w in data.get_neighbors(path[i]):
            if neighbor == path[i + 1]:
                cost += w
                break
    return cost

# data = GraphData()
# result = greedy(data, "Central", "Hung Hom")
# print(result, data.heuristic("Central", "Hung Hom"))