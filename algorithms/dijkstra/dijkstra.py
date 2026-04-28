import heapq
from data.data_loader import GraphData


def dijkstra(data: GraphData, src: str, des: str) -> dict | None:
    # Validate
    if not data.has_node(src):
        print(f"[Dijkstra] Unknown station: '{src}'")
        return None
    if not data.has_node(des):
        print(f"[Dijkstra] Unknown station: '{des}'")
        return None
    if src == des:
        return {"path": [src], "cost": 0.0, "explored": []}

    # Data structures
    fringe = [(0.0, src)]          # (cost, node)
    g_cost = {src: 0.0}            # best cost so far
    parent = {}                    # reconstruct path
    explored = []

    while fringe:
        cost, current = heapq.heappop(fringe)

        if cost > g_cost.get(current, float("inf")):
            continue

        explored.append(current)

        # Found goal
        if current == des:
            path = _reconstruct(parent, src, des)
            return {
                "path": path,
                "cost": round(cost, 4),
                "explored": explored
            }

        # Relax edges
        for neighbor, weight in data.get_neighbors(current):
            new_cost = cost + weight

            if new_cost < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(fringe, (new_cost, neighbor))

    return None


def _reconstruct(parent: dict, src: str, goal: str) -> list[str]:
    path = [goal]
    current = goal

    while current != src:
        current = parent[current]
        path.append(current)

    return list(reversed(path))

# data = GraphData()
# result = dijkstra(data, "Central", "Hung Hom")
# print(result)