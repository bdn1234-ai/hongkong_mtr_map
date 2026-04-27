import heapq
from data_loader import GraphData


def astar(data: GraphData, start: str, goal: str) -> dict | None:
    # Validate
    if not data.has_node(start):
        print(f"[A*] Unknown station: '{start}'")
        return None
    if not data.has_node(goal):
        print(f"[A*] Unknown station: '{goal}'")
        return None
    if start == goal:
        return {"path": [start], "cost": 0.0, "explored": []}

    # Data structures
    g = {start: 0.0}

    came_from = {}

    open_heap = [(data.heuristic(start, goal), start)]

    # Stations already fully explored
    closed = set()

    explored = []

    # Main loop 
    while open_heap:
        _, current = heapq.heappop(open_heap)

        if current in closed:   # stale heap entry → skip
            continue

        explored.append(current)
        closed.add(current)

        if current == goal:
            return {
                "path": _reconstruct(came_from, goal),
                "cost": round(g[goal], 4),
                "explored": explored,
            }

        for neighbor, edge_cost in data.get_neighbors(current):
            if neighbor in closed:
                continue

            tentative_g = g[current] + edge_cost

            if tentative_g < g.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f = tentative_g + data.heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f, neighbor))

    return None  # no path found


def _reconstruct(came_from: dict, current: str) -> list[str]:
    """Walk came_from backwards to build start → goal path."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))