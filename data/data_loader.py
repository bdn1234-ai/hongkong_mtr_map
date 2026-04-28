import json
import os

class GraphData:
    def __init__(self, graph_path=None, coords_path=None):
        if graph_path is None:
            graph_path = os.path.join(os.path.dirname(__file__), "processed_data", "graph.json")
        if coords_path is None:
            coords_path = os.path.join(os.path.dirname(__file__), "processed_data", "coords.json")
        
        with open(graph_path, "r", encoding="utf-8") as f:
            self.graph = json.load(f)

        with open(coords_path, "r", encoding="utf-8") as f:
            self.coords = json.load(f)

    def get_nodes(self):
        return list(self.graph.keys())
    
    def has_node(self, node):
        return node in self.graph
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def get_cost(self, u, v):
        for neighbor, cost in self.graph.get(u, []):
            if neighbor == v:
                return cost
        return float("inf")

    
    def get_coord(self, node):
        return self.coords.get(node, None)

    
    def heuristic(self, a, b):
        coord_a = self.get_coord(a)
        coord_b = self.get_coord(b)

        if not coord_a or not coord_b:
            return 0

    
        return abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])